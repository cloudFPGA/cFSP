# /*******************************************************************************
#  * Copyright 2016 -- 2022 IBM Corporation
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *     http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
# *******************************************************************************/

#  *
#  *                       cloudFPGA
#  *     Copyright IBM Research, All Rights Reserved
#  *    =============================================
#  *     Created: Mar. 2021
#  *     Authors: FAB, WEI, NGL, DID
#  *
#  *     Description:
#  *      A Python library with functions for accessing cFRM and create/delete images, instances, clusters etc.
#  *
#  *

import os
import sys
import requests
from requests.utils import requote_uri
import json
import time
import datetime

from cfsp_user import *
from cfsp_globals import *

from util import errorReqExit




####################################################################################################
# Clusters functions
####################################################################################################


class cFcluster:
    """Representation of a specific cloudFPGA cluster"""

    def __init__(self, user: cFuser, cluster_data):
        self.user = user
        self.cluster_data = cluster_data
        self.id = cluster_data['cluster_id']

    def get_id(self):
        return self.id


def post_cluster(user: cFuser, number_of_FPGA_nodes, role_image_id, host_address):
    # build cluster_req structure
    print("Creating FPGA cluster...")
    try:
        start = time.time()
        sw_rank = 0
        cluster_req = []
        rank0node = {'image_id': __NON_FPGA_IDENTIFIER__,
                     'node_id': sw_rank,
                     'node_ip': host_address}
        cluster_req.append(rank0node)
        size = number_of_FPGA_nodes + 1
        for i in range(1, size):
            fpgaNode = {
                'image_id': str(role_image_id),
                'node_id': i
            }
            cluster_req.append(fpgaNode)

        r1 = requests.post(
            "http://" + __cf_manager_url__ + "/clusters?{0}&dont_verify_memory=0".format(
                user.get_auth_string(with_project=True)),
            json=cluster_req, timeout=__POST_CLUSTER_TIMEOUT__)
        elapsed = time.time() - start

        if r1.status_code != 200:
            # something went wrong
            return errorReqExit("POST cluster", r1.status_code)

        cluster_data = json.loads(r1.text)
        print("Id of new cluster: {}".format(cluster_data['cluster_id']))
        print("Time for POST cluster: \t{0}s\n".format(elapsed))
        new_cluster = cFcluster(user, cluster_data)
        return new_cluster
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry
        print(e)
        print("ERROR: Something went wrong with post_cluster request and it reached timeout="+str(__POST_CLUSTER_TIMEOUT__)+". Maybe retry or increase timeout value.\n")
        sys.exit(1)


def get_cluster_data(cluster: cFcluster):
    print("Requesting cluster data for cluster_id={0} ...".format(cluster.get_id())) # FIXME: .get_id()
    try:
        start = time.time()
        r1 = requests.get(
            "http://" + __cf_manager_url__ + "/clusters/" + str(cluster.get_id()) + "?{0}".format(
                cluster.user.get_auth_string()), timeout=__GET_CLUSTER_TIMEOUT__)
        elapsed = time.time() - start
        print("Time for GET cluster: \t{0}s\n".format(elapsed))
        if r1.status_code != 200:
            # something went horrible wrong
            return errorReqExit("GET cluster", r1.status_code)

        cluster_data = json.loads(r1.text)
        # update, if necessary
        cluster.cluster_data = cluster_data
        return cluster_data
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry
        print(e)
        print("ERROR: Something went wrong with get_cluster_data request and it reached timeout="+str(__GET_CLUSTER_TIMEOUT__)+". Maybe retry or increase timeout value.\n")


def get_clusters_data(user: cFuser, limit=100):
    print("Requesting clusters data (limit="+str(limit)+")...")
    try:
        start = time.time()
        r1 = requests.get(
            "http://" + __cf_manager_url__ + "/clusters" + "?{0}&limit={1}".format(
                user.get_auth_string(), limit), timeout=__GET_CLUSTER_TIMEOUT__)
        elapsed = time.time() - start
        print(r1.request.url)
        print("Time for GET clusters: \t{0}s\n".format(elapsed))
        if r1.status_code != 200:
            # something went horrible wrong
            return errorReqExit("GET clusters", r1.status_code)
        clusters_data = json.loads(r1.text)
        return clusters_data
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry
        print(e)
        print("ERROR: Something went wrong with get_cluster request and it reached timeout="+str(__GET_CLUSTER_TIMEOUT__)+". Maybe retry or increase timeout value.\n")


def delete_cluster_data(cluster: cFcluster):
    print("Requesting delete cluster_id={0} ...".format(cluster.get_id()))
    try:
        start = time.time()
        r1 = requests.delete(
            "http://" + __cf_manager_url__ + "/clusters/" + str(cluster.get_id()) + "?{0}".format(
                cluster.user.get_auth_string()), timeout=__DELETE_CLUSTER_TIMEOUT__)
        elapsed = time.time() - start
        print("Time for DELETE cluster: \t{0}s\n".format(elapsed))
        if r1.status_code != 204:
            # something went horrible wrong
            return errorReqExit("DELETE cluster", r1.status_code)
        return 0
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry
        print(e)
        print("ERROR: Something went wrong with delete_cluster_data request and it reached timeout="+str(__DELETE_CLUSTER_TIMEOUT__)+". Maybe retry or increase timeout value.\n")


def restart_cluster_apps(cluster: cFcluster):
    print("Requesting restart for (all) FPGA(s) of cluster_id={0} ...".format(cluster.get_id()))
    try:
        start = time.time()        
        r1 = requests.patch(
            "http://" + __cf_manager_url__ + "/clusters/" + str(cluster.get_id()) + "/restart?{0}".format(
            cluster.user.get_auth_string()))
        elapsed = time.time() - start
        print("Time for RESTART cluster: \t{0}s\n".format(elapsed))

        if r1.status_code != 200:
            # something went horrible wrong
            return errorReqExit("PATCH cluster restart", r1.status_code)
        print(r1.content.decode())

    except Exception as e:
        print("ERROR: Failed to reset the FPGA(s) role(s)")
        print(str(e))
        exit(1)

####################################################################################################
# Instances functions
####################################################################################################


class cFinstance:

    def __init__(self, user: cFuser, instance_data):
        self.instance_data = instance_data
        self.user = user
        self.id = instance_data['instance_id']

    def get_id(self):
        return self.id
    
def get_instances_data(user: cFuser, limit=100):
    print("Requesting instances data (limit="+str(limit)+")...")
    try:
        start = time.time()
        r1 = requests.get(
            "http://" + __cf_manager_url__ + "/instances" + "?{0}&limit={1}".format(
                user.get_auth_string(), limit), timeout=__GET_INSTANCE_TIMEOUT__)
        elapsed = time.time() - start
        print(r1.request.url)
        print("Time for GET instances: \t{0}s\n".format(elapsed))
        if r1.status_code != 200:
            # something went horrible wrong
            return errorReqExit("GET instances", r1.status_code)
        instances_data = json.loads(r1.text)
        return instances_data
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry
        print(e)
        print("ERROR: Something went wrong with get_instances request and it reached timeout="+str(__GET_INSTANCE_TIMEOUT__)+". Maybe retry or increase timeout value.\n")

def create_instance():
    print("TODO \n")


def get_instance_data(instance: cFinstance):
    print("Requesting instance data for instance_id={0} ...".format(instance.get_id()))
    try:
        start = time.time()
        r1 = requests.get(
            "http://" + __cf_manager_url__ + "/instances/" + str(instance.get_id()) + "?{0}".format(
                instance.user.get_auth_string()), timeout=__GET_INSTANCE_TIMEOUT__)
        elapsed = time.time() - start
        print("Time for GET instance: \t{0}s\n".format(elapsed))
        if r1.status_code != 200:
            # something went horrible wrong
            return errorReqExit("GET instance", r1.status_code)

        instance_data = json.loads(r1.text)
        # update, if necessary
        instance.instance_data = instance_data
        return instance_data
    except requests.exceptions.Timeout as e:
        # Maybe set up for a retry
        print(e)
        print("ERROR: Something went wrong with get_instance_data request and it reached timeout="+str(__GET_INSTANCE_TIMEOUT__)+". Maybe retry or increase timeout value.\n")



def reprogram_instance():
    print("TODO \n")


def api_request_instance():
    print("TODO \n")


def restart_instance_app(instance: cFinstance):
    print("Requesting restart for instance_id={0} ...".format(instance.get_id()))
    try:
        start = time.time()       
        r1 = requests.patch(
            "http://" + __cf_manager_url__ + "/instances/" + str(instance.get_id()) + "/app_restart?{0}".format(
            instance.user.get_auth_string()))
        elapsed = time.time() - start
        print("Time for RESTART instance: \t{0}s\n".format(elapsed))

        if r1.status_code != 200:
            # something went horrible wrong
            return errorReqExit("PATCH instance restart", r1.status_code)
        print(r1.content.decode())

    except Exception as e:
        print("ERROR: Failed to reset the FPGA role")
        print(str(e))
        exit(1)

def delete_instance(instance: cFinstance):
    print("deleting instance {}".format(instance.id))

    r1 = requests.delete(
        "http://" + __cf_manager_url__ + "/instances/{0}?{1}".format(instance.id, instance.user.get_auth_string()))

    if r1.status_code > 204:
        # error codes
        # 204 Instance was deleted
        # 401 Unauthenticated, bad login
        # 403 Unauthorized
        # 404 Instance does not exist
        return r1.status_code
    else:
        print("Instance {} removed".format(instance.id))

    instance_data = r1.status_code
    return instance_data


####################################################################################################
# Images functions
####################################################################################################

class cFimage:

    def __init__(self, user: cFuser, image_data):
        self.user = user
        self.image_data = image_data
        self.id = image_data['id']
        self.comment = image_data['comment']
        self.required_shell = image_data['shell_type']


def get_images(user: cFuser):
    print("TODO \n")


def get_image(image: cFimage):
    print("TODO \n")


def post_image(image: cFimage):
    print("TODO \n")


def delete_image(image: cFimage):
    print("TODO \n")


####################################################################################################
# Resources functions (admin only)
####################################################################################################

# TODO: no resource class so far, because the resource data should reside inside the CFRM, not the cFSP

def get_resource_status(resource_id, admin: cFuser):
    print("Requesting resource status...")
    r1 = requests.get(
        "http://" + __cf_manager_url__ + "/resources/" + str(
            resource_id) + "/status/" + "?{0}".format(admin.get_auth_string()))

    if r1.status_code != 200:
        # something went wrong
        return errorReqExit("GET resource status", r1.status_code)

    resource_status = json.loads(r1.text)
    return resource_status


def set_resource_status(resource_id, new_status, admin: cFuser):
    # print("set resource status")

    # possible status: "AVAILABLE", "USED", "MAINTENANCE"
    r1 = requests.put(
        "http://" + __cf_manager_url__ + "/resources/{0}/status/?{1}&new_status={2}".format(
            resource_id, admin.get_auth_string(), new_status))

    if r1.status_code != 204:
        # something went wrong
        return errorReqExit("PUT /resources/{resource_id}/status/", r1.status_code)
    else:
        print("Resource {} set to {}".format(resource_id, new_status))

    resource_data = r1.status_code
    return resource_data


