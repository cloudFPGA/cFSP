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
    cfsp debug (get)    
Commands:
    get flight_recorder_data <cluster/instance>   Requests and returns the status information of the 
                                            Network Routing Core of this cluster/instance
                                            Attention: There may be a delay of a few seconds until 
                                            the counters are updated after the packets were 
                                            processed. 
"""
from __future__ import absolute_import

import sys,os
python_api_client_path = os.getcwd()+"/cFSPlib/python_api_client/"
sys.path.append(python_api_client_path)

import cfsp_globals
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from tqdm import tqdm

def main(args):
    conf = Configuration()
    conf.host = cfsp_globals.__cf_manager_url__
    api_client = ApiClient(conf)    
    api_instance = swagger_client.DebugApi(api_client=api_client)

    if (len(args['<args>']) != 4):
        print("ERROR: invalid arguments provided in 'cfsp debug' command. Aborting...")
        exit(print(__doc__))
    
    username = cfsp_globals.__cfsp_username__
    password = cfsp_globals.__cfsp_password__
    project_name = cfsp_globals.__cfsp_project__
    
    if args['<args>'][0] == 'get':
        if (args['<args>'][1] == "flight_recorder_data"):
            if args['<args>'][2] == 'cluster':
                try:
                    api_response = api_instance.cf_manager_rest_api_get_flight_recorder_cluster(username, password, args['<args>'][3])
                except ApiException as e:
                    print("Exception when calling DebugApi->cf_manager_rest_api_get_flight_recorder_cluster: %s\n" % e)              
                    exit(-1)
            elif args['<args>'][2] == 'instance':
                try:
                    api_response = api_instance.cf_manager_rest_api_get_flight_recorder_instance(username, password, args['<args>'][3])
                except ApiException as e:
                    print("Exception when calling DebugApi->cf_manager_rest_api_get_flight_recorder_instance: %s\n" % e)              
                    exit(-1)                      
            else:
                exit(print("ERROR: invalid arguments provided in cfsp debug get flight_recorder_data. Choose between 'cluster' or 'instance'. Aborting..."))
        else:
            exit(print("ERROR: invalid arguments provided in cfsp debug get. Aborting..."))
        return(api_response)
    else:
        exit(print("ERROR: invalid command provided in cfsp debug. Type 'cfsp help debug' to get a list of supported commands. Aborting..."))
if __name__ == '__main__':
    main(args)
