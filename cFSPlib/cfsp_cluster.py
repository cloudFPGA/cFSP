"""usage: cfsp cluster (get | post) [credentials_file]
"""
from __future__ import absolute_import

import sys,os
python_api_client_path = os.getcwd()+"/cFSPlib/python_api_client/"
sys.path.append(python_api_client_path)

import cfsp_globals
import swagger_client
from swagger_client.api.clusters_api import ClustersApi  # noqa: E501
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration


def main(args):
    print("cluster main")

    conf = Configuration()
    conf.host = cfsp_globals.__cf_manager_url__
    api_client = ApiClient(conf)    
    cluster_api = ClustersApi(api_client=api_client) 

    if ((len(args['<args>']) < 1) or (len(args['<args>']) > 2)):
        print("ERROR: invalid arguments provided in 'cfsp cluster' command. Aborting...")
        exit(print(__doc__))
    
    print(args['<args>'])
    if args['<args>'][0] == 'get':
        print("cluster get")
        username = cfsp_globals.__cfsp_username__
        password = cfsp_globals.__cfsp_password__
        print('username='+username)
        if (len(args['<args>']) == 2):
            returned = cluster_api.cf_manager_rest_api_get_cluster_single(username, password, args['<args>'][1])
        elif (len(args['<args>']) == 1):
            returned = cluster_api.cf_manager_rest_api_get_clusters(username, password)
        else:
            exit(print("ERROR: invalid arguments provided in cfsp cluster get. Aborting..."))
        print(returned)




    
    
if __name__ == '__main__':
    main(args)
