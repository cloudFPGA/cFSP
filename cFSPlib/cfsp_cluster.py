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
    cfsp cluster (get | post | extend | update | delete)    
Commands:
    get <id>     Get all clusters of a user. Either <id> of cluster or no argument for all.
    post         Request a cluster.
    extend id    Add nodes to an existing cluster
    update id    Reconfigure one FPGA node of an existing cluster  
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
        return(api_response)
    elif (args['<args>'][0] == 'post') or (args['<args>'][0] == 'extend'):
        # create an instance of the API class
        body = []        
        cpu_num = len(args['--node_ip'])
        fpga_num = len(args['--image_id'])
        node_id_num = len(args['--node_id'])
        
        if node_id_num == 0:
            print("WARNING: No --node_id argument was provided. Incremental ids will be used for fpga(s) and cpu(s) in this cluster.")
            for i in range(fpga_num):
                args['--node_id'].append(i)
            for j in range(cpu_num):
                args['--node_id'].append(fpga_num+j)
        else:
            if (node_id_num != cpu_num + fpga_num):
                exit(print("ERROR: The provided argument(s) of --node_id ("+str(node_id_num)+") is not the same with the sum of --node_ip ("+str(cpu_num)+") and --image_id ("+str(fpga_num)+") ones. Please note that for each of --node_ip and --image_id, a --node_id argument is required. Aborting..."))
        
        # Convert the node_id list to ints
        args['--node_id'] = list(map(int, args['--node_id']))
   
        print("INFO: Please review the assignment of image_id(s), node_ip(s) and node_id(s)")
        print("[image_id, node_id]")
        for i in range(fpga_num):
            fpga_body = {    "image_id": args['--image_id'][i],  "node_id": args['--node_id'][i] }
            print("["+args['--image_id'][i] + ", " + str(args['--node_id'][i]) + "]")
            body.append(fpga_body)
        print("[node_ip, node_id]")            
        for j in range(cpu_num):
            cpu_body = {    "image_id": cfsp_globals.__NON_FPGA_IDENTIFIER__,    "node_ip":  args['--node_ip'][j],    "node_id": args['--node_id'][fpga_num+j] }
            print("["+args['--node_ip'][j] + ", " + str(args['--node_id'][fpga_num+j]) + "]")
            body.append(cpu_body)
        
        if (args['<args>'][0] == 'post'):
            try:
                # Request a cluster
                api_response = api_instance.cf_manager_rest_api_post_clusters(body, username, password, project_name=project_name, dont_verify_memory=args['--dont_verify_memory'])
                return(api_response)
            except ApiException as e:
                print("Exception when calling ClustersApi->cf_manager_rest_api_post_clusters: %s\n" % e)
                exit(-1)
        elif args['<args>'][0] == 'extend':
            try:
                # Request to extend cluster
                api_response = api_instance.cf_manager_rest_api_extend_cluster(body, username, password, cluster_id=args['--cluster_id'], dont_verify_memory=args['--dont_verify_memory'])
                return(api_response)
            except ApiException as e:
                print("Exception when calling ClustersApi->cf_manager_rest_api_extend_cluster: %s\n" % e)
                exit(-1)
    elif (args['<args>'][0] == 'reduce'):
        node_id_num = len(args['--node_id'])
        body = []
        
        # Convert the node_id list to ints
        args['--node_id'] = list(map(int, args['--node_id']))
        
        for i in range(node_id_num):
            node_id_body = args['--node_id'][i]
            body.append(node_id_body)
        try:
            # Request to extend cluster
            api_response = api_instance.cf_manager_rest_api_reduce_cluster(body, username, password, cluster_id=args['--cluster_id'])
            return(api_response)
        except ApiException as e:
            print("Exception when calling ClustersApi->cf_manager_rest_api_reduce_cluster: %s\n" % e)
            exit(-1)
    elif (args['<args>'][0] == 'update'):
        node_id_num = len(args['--node_id'])
        cpu_num = len(args['--node_ip'])
        fpga_num = len(args['--image_id'])
        try:
            cluster_id_num = len(args['--cluster_id'])
        except:
            exit(print("ERROR: The argument --cluster_id must be provided once. Aborting..."))
            
        
        if (cpu_num != 0):
            exit(print("ERROR: Irrelevant argument --node_ip in cluster update. Aborting..."))
        if (fpga_num != 1):
            exit(print("ERROR: The argument --image_id must be provided once. Aborting..."))
        if (node_id_num == 0):
            print("WARNING: No argument --node_id was provided. Will try to locate FPGA node_id's in cluster "+ str(args['--cluster_id'])+ " ...")
            try:
                api_response = api_instance.cf_manager_rest_api_get_cluster_single(username, password, args['--cluster_id'])
            except ApiException as e:
                print("Exception when calling ClustersApi->cf_manager_rest_api_get_cluster_single: %s\n" % e)              
                exit(-1)            
            
            nodes_in_cluster_len = len(api_response.nodes)
            for i in range(nodes_in_cluster_len):
                #if (api_response.nodes[i].['image_id'] != 'NON_FPGA'):
                if (api_response.nodes[i].get('image_id')!= 'NON_FPGA'):
                    print("INFO: Found FPGA node at id: " + str(api_response.nodes[i].get('node_id')))
                    args['--node_id'].append(api_response.nodes[i].get('node_id'))
        else:
            # Convert the node_id list to ints
            args['--node_id'] = list(map(int, args['--node_id']))
            
        node_id_num = len(args['--node_id'])
            
        for i in range(node_id_num):
            try:
                # Request to update cluster
                api_response = api_instance.cf_manager_rest_api_update_node_of_cluster(args['--image_id'][0], username, password, cluster_id=args['--cluster_id'], node_id=args['--node_id'][i], dont_verify_memory=args['--dont_verify_memory'])
            except ApiException as e:
                print("Exception when calling ClustersApi->cf_manager_rest_api_update_node_of_cluster: %s\n" % e)
                exit(-1)
        # We just return the last responce since it returns the whole cluster
        return(api_response)
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
                 api_response = api_instance.cf_manager_rest_api_delete_cluster(username, password, cluster_id)
                 return(api_response)
            except ApiException as e:
                print("Exception when calling ClustersApi->cf_manager_rest_api_delete_cluster: %s\n" % e)
                exit(-1)
        else:
            exit(print("ERROR: invalid arguments provided in cfsp cluster delete. Aborting..."))
    else:
        exit(print("ERROR: invalid command provided in cfsp cluster. Type 'cfsp help cluster' to get a list of supported commands. Aborting..."))            

if __name__ == '__main__':
    main(args)
