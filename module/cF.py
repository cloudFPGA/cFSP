#  *
#  *                       cloudFPGA
#  *     Copyright IBM Research, All Rights Reserved
#  *    =============================================
#  *     Created: Sep. 2020
#  *     Authors: FAB, WEI, NGL, DID
#  *
#  *     Description:
#  *      A Python library with functions for accessing cFRM and create/delete images. clusters etc.
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

__openstack_pw__ = "XX"
__openstack_user__ = "YY"


__credentials_file_name__ = "user.json"

__openstack_user_template__ = {}
__openstack_user_template__['credentials'] = {}
__openstack_user_template__['credentials']['user'] = "your user name"
__openstack_user_template__['credentials']['pw'] = "your user password"

__cf_manager_url__ = "10.12.0.132:8080"
__NON_FPGA_IDENTIFIER__ = "NON_FPGA"


def print_usage():
    print("Openstack credentials should be stored in {}) \n".format(__credentials_file_name__) +
          "Options available in cF library :\n" +
          " - post_cluster(number_of_FPGA_nodes, role_image_id, host_address)\n" +
          " - get_cluster_data(cluster_id) \n" +
          " - get_clusters_data() \n" +
          " - delete_cluster_data(cluster_id) \n" +
          " - load_user_credentials(filedir) \n" +
          " - show_user_credentials(filedir) \n")
    exit(1)


def errorReqExit(msg,code):
    print("Request "+msg+" failed with HTTP code "+str(code)+".")
    if (msg=="GET cluster") or (msg=="GET clusters") or (msg=="DELETE cluster"):
      if (code==400):
	print("400 Bad request (maybe login/pass with space char?)\n")
      if (code==401):
	print("401 Unauthenticated, bad login\n")
      if (code==403):
	print("403 Unauthorized\n")
      if (code==404):
	print("404 Cluster does not exist\n")
    exit(1)



####################################################################################################  
# Clusters functions
####################################################################################################  

def post_cluster(number_of_FPGA_nodes, role_image_id, host_address):
    # build cluster_req structure
    print("Creating FPGA cluster...")
    start = time.time()
    sw_rank = 0
    cluster_req = []
    rank0node = {'image_id': __NON_FPGA_IDENTIFIER__,
                 'node_id': sw_rank,
                 'node_ip': host_address}
    cluster_req.append(rank0node)
    size = number_of_FPGA_nodes+1
    for i in range(1, size):
        fpgaNode = {
            'image_id': str(role_image_id),
            'node_id': i
        }
        cluster_req.append(fpgaNode)

    r1 = requests.post("http://"+__cf_manager_url__+"/clusters?username={0}&password={1}&project_name=cf_Test_2".format(__openstack_user__,__openstack_pw__),
                       json=cluster_req)
    elapsed = time.time() - start
    
    if r1.status_code != 200:
        # something went horrible wrong
        return errorReqExit("POST cluster", r1.status_code)

    cluster_data = json.loads(r1.text)
    print("Id of new cluster: {}".format(cluster_data['cluster_id']))
    print("Time for POST cluster: \t{0}s\n".format(elapsed))
    return cluster_data


def get_cluster_data(cluster_id):
    print("Requesting cluster data for cluster_id={0} ...".format(cluster_id))
    start = time.time()
    r1 = requests.get("http://"+__cf_manager_url__+"/clusters/"+str(cluster_id)+"?username={0}&password={1}".format(__openstack_user__,__openstack_pw__))
    elapsed = time.time() - start
    print("Time for GET cluster: \t{0}s\n".format(elapsed))
    if r1.status_code != 200:
        # something went horrible wrong
        return errorReqExit("GET cluster", r1.status_code)

    cluster_data = json.loads(r1.text)
    return cluster_data


  
def get_clusters_data():
    print("Requesting clusters data (limit=100)...")
    start = time.time()
    r1 = requests.get("http://"+__cf_manager_url__+"/clusters"+"?username={0}&password={1}&limit=100".format(__openstack_user__,__openstack_pw__))
    elapsed = time.time() - start
    print("Time for GET clusters: \t{0}s\n".format(elapsed))  
    if r1.status_code != 200:
        # something went horrible wrong
        return errorReqExit("GET clusters", r1.status_code)

    clusters_data = json.loads(r1.text)
    return clusters_data
  

def delete_cluster_data(cluster_id):
    print("Requesting delete cluster_id={0} ...".format(cluster_id))
    start = time.time()
    r1 = requests.delete("http://"+__cf_manager_url__+"/clusters/"+str(cluster_id)+"?username={0}&password={1}".format(__openstack_user__,__openstack_pw__))
    elapsed = time.time() - start
    print("Time for DELETE cluster: \t{0}s\n".format(elapsed))
    if r1.status_code != 204:
        # something went horrible wrong
        return errorReqExit("DELETE cluster", r1.status_code)

    cluster_data = json.loads(r1.text)
    return cluster_data
  
  
  
####################################################################################################  
# Login functions
####################################################################################################  

def load_user_credentials(filedir):
    json_file = filedir + "/" + __credentials_file_name__
    global __openstack_user__
    global __openstack_pw__

    try:
        with open(json_file, 'r') as infile:
            data = json.load(infile)
        __openstack_user__ = data['credentials']['user']
        __openstack_pw__ = data['credentials']['pw']
        return 0
    except Exception as e:
        print(e)
        print("Writing credentials template to {}\n".format(json_file))

    with open(json_file, 'w') as outfile:
        json.dump(__openstack_user_template__, outfile)
    return -1


def show_user_credentials(filedir):
    json_file = filedir + "/" + __credentials_file_name__
    global __openstack_user__
    global __openstack_pw__

    try:
        print("User     : "+__openstack_user__)
        print("Password : "+__openstack_pw__)
        return 0
    except Exception as e:
        print(e)
        print("No credentials found \n")

  

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

