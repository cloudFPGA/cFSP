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
#  *     Created: Sep. 2020
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

# __openstack_pw__ = "XX"
# __openstack_user__ = "YY"
# __credentials_file_name__ = "user.json"

from util import print_usage, errorReqExit

import mngmt
import comm

####################################################################################################
# Instances functions
####################################################################################################

def get_instances_data():
    print("TODO \n")


def create_instance():
    print("TODO \n")


def get_instance_data():
    print("TODO \n")


def reprogram_instance():
    print("TODO \n")


def api_request_instance():
    print("TODO \n")


def restart_instance_app(instance_id):
    print("Restart FPGA ...")
    r1 = requests.patch(
        "http://" + __cf_manager_url__ + "/instances/" + str(instance_id) + "/restart?username={0}&password={1}".format(
            __openstack_user__, __openstack_pw__))

    if r1.status_code != 200:
        # something went horrible wrong
        return errorReqExit("PATCH instance restart", r1.status_code)

    instance_data = json.loads(r1.text)
    return instance_data


def delete_instance(resource_id):
    print("deleting instance {}".format(resource_id))

    r1 = requests.delete(
        "http://" + __cf_manager_url__ + "/instances/{0}?username={1}&password={2}".format(resource_id,
            __openstack_user__, __openstack_pw__))

    if r1.status_code > 204:
        # error codes
        # 204 Instance was deleted
        # 401 Unauthenticated, bad login
        # 403 Unauthorized
        # 404 Instance does not exist
        return r1.status_code
    else:
        print("Instance {} removed".format(resource_id))

    instance_data = r1.status_code
    return instance_data



####################################################################################################  
# Images functions
####################################################################################################  

def get_images():
    print("TODO \n")


def get_image(image_id):
    print("TODO \n")


def post_image(image_id):
    print("TODO \n")


def delete_image(image_id):
    print("TODO \n")


####################################################################################################
# Resources functions (admin only)
####################################################################################################

def get_resource_status(resource_id):
    print("Requesting resource status...")
    r1 = requests.get(
        "http://" + __cf_manager_url__ + "/resources/" + str(
            resource_id) + "/status/" + "?username={0}&password={1}".format(
            __openstack_user__, __openstack_pw__))

    if r1.status_code != 200:
        # something went horrible wrong
        return errorReqExit("GET resource status", r1.status_code)

    resource_status = json.loads(r1.text)
    return resource_status


def set_resource_status(resource_id, new_status):
    # print("set resource status")

    # possible status: "AVAILABLE", "USED", "MAINTENANCE"
    r1 = requests.put(
        "http://" + __cf_manager_url__ + "/resources/{0}/status/?username={1}&password={2}&new_status={3}"
        .format(resource_id, __openstack_user__, __openstack_pw__, new_status))

    if r1.status_code != 204:
        # something went horrible wrong
        return errorReqExit("PUT /resources/{resource_id}/status/", r1.status_code)
    else:
        print("Resource {} set to {}".format(resource_id, new_status))

    resource_data = r1.status_code
    return resource_data
