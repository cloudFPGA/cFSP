# *****************************************************************************
# *                            cloudFPGA
# *                Copyright 2016 -- 2022 IBM Corporation
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *     http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# *----------------------------------------------------------------------------

"""
Usage: 
    cfsp cluster (get | post | delete)    
Commands:
    get <id>     Get all clusters of a user. Either <id> of cluster or no argument for all.
    post         Request a cluster.
    delete id    Delete a cluster with cluster_id=id. If no id is provided then all clusters are deleted (after confirmation dialog with user)
"""
from __future__ import absolute_import

import sys,os
#python_api_client_path = os.getcwd()+"/cFSPlib/python_api_client/"
python_api_client_path = os.path.dirname(os.path.abspath(__file__))+"/python_api_client/"

sys.path.append(python_api_client_path)

import cfsp_globals
import swagger_client
from swagger_client.api.clusters_api import ClustersApi  # noqa: E501
from swagger_client.rest import ApiException
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from pprint import pprint
from tqdm import tqdm

def confirm_choice():
    confirm = input("[c]Confirm or [v]Void: ")
    if confirm != 'c' and confirm != 'v':
        print("\n Invalid Option. Please Enter a Valid Option.")
        return confirm_choice() 
    print (confirm)
    return confirm


def main(args):
    conf = Configuration()
    conf.host = cfsp_globals.__cf_manager_url__
    api_client = ApiClient(conf)    
    api_instance = ClustersApi(api_client=api_client) 

    if ((len(args['<args>']) < 1) or (len(args['<args>']) > 2)):
        print("ERROR: invalid arguments provided in 'cfsp cluster' command. Aborting...")
        exit(print(__doc__))
    
    username = cfsp_globals.__cfsp_username__
    password = cfsp_globals.__cfsp_password__
    project_name = cfsp_globals.__cfsp_project__

    if args['<args>'][0] == 'get':
        if (len(args['<args>']) == 2):
            try:
                api_response = api_instance.cf_manager_rest_api_get_cluster_single(username, password, args['<args>'][1])
            except ApiException as e:
                print("Exception when calling ClustersApi->cf_manager_rest_api_get_cluster_single: %s\n" % e)              
                exit(-1)
        elif (len(args['<args>']) == 1):
            try:
                api_response = api_instance.cf_manager_rest_api_get_clusters(username, password, limit=args['--limit'])
            except ApiException as e:
                print("Exception when calling ClustersApi->cf_manager_rest_api_get_clusters: %s\n" % e)              
                exit(-1)            
        else:
            exit(print("ERROR: invalid arguments provided in cfsp cluster get. Aborting..."))
        pprint(api_response)
    elif args['<args>'][0] == 'post':
        # create an instance of the API class
        # FIXME: Currently we only support a cluster with one ZYC2 VM and one FPGA
        body = [] #[swagger_client.ClustersBody, swagger_client.ClustersBody]        
        #body[0].image_id = args['--image_id']
        #body[0].node_id = 0
        #body[1] =  {    "image_id": "NON_FPGA",    "node_ip":  args['--node_ip'],    "node_id": 1  }
        
        fpga_num = len(args['--image_id'])
        for i in range(fpga_num):
            fpga_body = {    "image_id": args['--image_id'][i],  "node_id": i  }
            body.append(fpga_body)
            
        cpu_num = len(args['--node_ip'])
        for j in range(cpu_num):
            cpu_body = {    "image_id": cfsp_globals.__NON_FPGA_IDENTIFIER__,    "node_ip":  args['--node_ip'][j],    "node_id": fpga_num+j  }
            body.append(cpu_body)

        try:
            # Request a cluster
            api_response = api_instance.cf_manager_rest_api_post_clusters(body, username, password, project_name=project_name, dont_verify_memory=args['--dont_verify_memory'])
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ClustersApi->cf_manager_rest_api_post_clusters: %s\n" % e)
            exit(-1)
    elif args['<args>'][0] == 'delete':
        if (len(args['<args>']) == 1):
            print("INFO: Really deleting all clusters ?")
            if confirm_choice() == 'c':
                print("INFO: Confirmed deleting all clusters")
                try:
                    api_response_get_in_delete = api_instance.cf_manager_rest_api_get_clusters(username, password)
                    if(len(api_response_get_in_delete) > 0):
                        for this_cluster in tqdm(api_response_get_in_delete):                                  
                            # Delete a cluster
                            print("INFO: Deleting cluster " + str(this_cluster.cluster_id) + " ... ")
                            try:
                                api_instance.cf_manager_rest_api_delete_cluster(username, password, this_cluster.cluster_id)
                            except ApiException as e_in_delete:
                                print("Exception when calling ClustersApi->cf_manager_rest_api_delete_cluster: %s\n" % e_in_delete)        
                    else:
                        print("INFO: No clusters to delete.")
                except ApiException as e_in_get:
                    print("Exception when calling ClustersApi->cf_manager_rest_api_get_clusters: %s\n" % e_in_get)              
                    exit(-1)
            else:
                print ("INFO: Canceling deleting all clsuters")
        elif (len(args['<args>']) == 2):
            cluster_id = args['<args>'][1]
            # Delete a cluster
            print("INFO: Deleting cluster " + str(cluster_id) + " ... ")
            try:
                api_instance.cf_manager_rest_api_delete_cluster(username, password, cluster_id)
            except ApiException as e:
                print("Exception when calling ClustersApi->cf_manager_rest_api_delete_cluster: %s\n" % e)
                exit(-1)
        else:
            exit(print("ERROR: invalid arguments provided in cfsp cluster delete. Aborting..."))
    else:
        exit(print("ERROR: invalid command provided in cfsp cluster. Type 'cfsp help cluster' to get a list of supported commands. Aborting..."))            

if __name__ == '__main__':
    main(args)
