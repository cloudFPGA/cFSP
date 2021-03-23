# /*******************************************************************************
#  * Copyright 2016 -- 2021 IBM Corporation
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
import subprocess
import requests
import json
import time
import resource
import datetime

from util import errorReqExit

####################################################################################################
# Global Constants
####################################################################################################

__openstack_user_template__ = {}
__openstack_user_template__['credentials'] = {}
__openstack_user_template__['credentials']['user'] = "your user name"
__openstack_user_template__['credentials']['pw'] = "your user password"
__openstack_user_template__['project'] = "default"

__cf_manager_url__ = "10.12.0.132:8080"
__NON_FPGA_IDENTIFIER__ = "NON_FPGA"

__POST_CLUSTER_TIMEOUT__   = 130
__GET_CLUSTER_TIMEOUT__    = 5
__DELETE_CLUSTER_TIMEOUT__ = 20


####################################################################################################
# User functions
####################################################################################################

class cFuser:
    """A user in the cloudFPGA world"""

    def __init__(self, credentials_path):
        user, pw, project = load_user_credentials(credentials_path)
        self.user = user
        self.pw = pw
        self.project = project

    def get_auth_string(self, with_project=False):
        if with_project:
            s = "username={0}&password={1}&project_name={2}".format(self.user, self.pw, self.project)
            return s
        else:
            s = "username={0}&password={1}".format(self.user, self.pw)
            return s

    def set_project(self, new_project):
        """
        This method should be used if the cloudFPGA quota name that should be used for this handle is different from the
        default or credentials file
        :param new_project:
        :return: nothing
        """
        self.project = new_project

    def show_credentials(self):
        print("User     : " + self.user)
        print("Password : " + self.pw)
        print("Project  : " + self.project)


def load_user_credentials(json_file):
    user = ""
    pw = ""
    project = ""

    try:
        with open(json_file, 'r') as infile:
            data = json.load(infile)
        user = data['credentials']['user']
        pw = data['credentials']['pw']
        if 'project' in data:
            project = data['project']
        else:
            project = __openstack_user_template__['project']
        return user, pw, project
    except Exception as e:
        print(e)
        print("Writing credentials template to {}\n".format(json_file))

    with open(json_file, 'w') as outfile:
        json.dump(__openstack_user_template__, outfile)
    sys.exit(1)


def show_user_credentials(json_file):
    try:
        with open(json_file, 'r') as infile:
            data = json.load(infile)
        user = data['credentials']['user']
        pw = data['credentials']['pw']
        if 'project' in data:
            project = data['project']
        else:
            project = __openstack_user_template__['project']
        print("User     : " + user)
        print("Password : " + pw)
        print("Project  : " + project)
        return 0
    except Exception as e:
        print(e)
        print("No credentials found \n")
        sys.exit(1)


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
    print("Requesting cluster data for cluster_id={0} ...".format(cluster.get_id()))
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
    print("Restart all FPGAs ...")
    r1 = requests.patch(
        "http://" + __cf_manager_url__ + "/clusters/" + str(cluster.get_id()) + "/restart?{0}".format(
            cluster.user.get_auth_string()))

    if r1.status_code != 200:
        # something went horrible wrong
        return errorReqExit("PATCH cluster restart", r1.status_code)

    cluster_data = json.loads(r1.text)
    # update, if necessary
    cluster.cluster_data = cluster_data
    return cluster_data

