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

####################################################################################################
# Utility Functions
####################################################################################################


def print_usage():
    print( # "Openstack credentials should be stored in {}) \n".format(__credentials_file_name__) +
        "Options available in cF library :\n" +
        " - Clusters: \n" +
        "   - post_cluster(number_of_FPGA_nodes, role_image_id, host_address)\n" +
        "   - get_cluster_data(cluster_id) \n" +
        "   - get_clusters_data(limit) \n" +
        "   - delete_cluster_data(cluster_id) \n" +
        "   - restart_cluster_apps(cluster_id) \n" +
        " - Instances: \n" +
        "   - restart_instance_app(instance_id) \n" +
        "   - delete_instance(resource_id) \n" +
        " - Resources: \n" +
        "   - get_resource_status(resource_id) \n" +
        " - Users: \n" +
        "   - load_user_credentials(filedir) \n" +
        "   - show_user_credentials(filedir) \n\n")
    #exit(1)


def errorReqExit(msg, code):
    print("Request " + msg + " failed with HTTP code " + str(code) + ".")
    if code == 0:
        print("0 error: no response from server\n")
    elif (msg == "GET cluster") or (msg == "GET clusters") or (msg == "DELETE cluster"):
        if code == 400:
            print("400 Bad request (maybe login/pass with space char?)\n")
        if code == 401:
            print("401 Unauthenticated, bad login\n")
        if code == 403:
            print("403 Unauthorized\n")
        if code == 404:
            print("404 Cluster does not exist\n")
    elif msg == "POST cluster":
        if code == 401:
            print("401 Unauthenticated, bad login\n")
        if code == 404:
            print("404 One of the regested images does not exist\n")
        if code == 415:
            print("415 Image has wrong type/breed\n")
        if code == 422:
            print("422 Malformed request\n")
        if code == 424:
            print("424 Bitfile seems to be preecarious/unstable (e.g. bad timing or could also hide an internal server error)\n")
        if code == 429:
            print("429 Insufficient Quota\n")
        if code == 500:
            print("500 Error in communication with devices (maybe try again)\n")
        if code == 503:
            print("503 No resources available to fullfil the request\n")
        if code == 507:
            print("507 Network or Memory failure on target device (maybe try again)\n")
        if code == 508:
            print("508 No network resources available, please contact admins\n")
    exit(1)


