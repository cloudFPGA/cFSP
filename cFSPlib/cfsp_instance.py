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
    cfsp instance (get | post | delete)    
Commands:
    get <id>     Get all instances of a user. Either <id> of instance or no argument for all.
    post         Request an instance.
    delete id    Delete an instance with instance_id=id. If no id is provided then all instances are deleted (after confirmation dialog with user)
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
    api_instance = swagger_client.InstancesApi(api_client=api_client)

    if ((len(args['<args>']) < 1) or (len(args['<args>']) > 2)):
        print("ERROR: invalid arguments provided in 'cfsp instance' command. Aborting...")
        exit(print(__doc__))
    
    username = cfsp_globals.__cfsp_username__
    password = cfsp_globals.__cfsp_password__
    project_name = cfsp_globals.__cfsp_project__
    
    if args['<args>'][0] == 'get':
        if (len(args['<args>']) == 2):
            try:
                api_response = api_instance.cf_manager_rest_api_get_instance(username, password, args['<args>'][1])
            except ApiException as e:
                print("Exception when calling InstancesApi->cf_manager_rest_api_get_instance: %s\n" % e)              
                exit(-1)
        elif (len(args['<args>']) == 1):
            try:
                api_response = api_instance.cf_manager_rest_api_get_instances(username, password, limit=args['--limit'])
            except ApiException as e:
                print("Exception when calling InstancesApi->cf_manager_rest_api_get_instances: %s\n" % e)              
                exit(-1)            
        else:
            exit(print("ERROR: invalid arguments provided in cfsp instance get. Aborting..."))
        return(api_response)
    elif args['<args>'][0] == 'post':
        # create an instance of the API class
        if len(args['--image_id']) != 1:
            exit(print("ERROR: instance post supports only one image (--image_id). Aborting..."))
        image_id = args['--image_id'][0]
        try:
            # Request an instance
            api_response = api_instance.cf_manager_rest_api_post_instances(image_id, username, password, project_name=project_name, dont_verify_memory=args['--dont_verify_memory'])
            # post_instance dows not return the role_ip, thus we call get_instance afterwards.
            instance_id = api_response.instance_id
            try:
                api_response = api_instance.cf_manager_rest_api_get_instance(username, password, instance_id)
            except ApiException as e:
                print("Exception when calling InstancesApi->cf_manager_rest_api_get_instance: %s\n" % e)              
                exit(-1)
            return(api_response)
        except ApiException as e:
            print("Exception when calling InstancesApi->cf_manager_rest_api_post_instances: %s\n" % e)
            exit(-1)
    elif args['<args>'][0] == 'delete':
        if (len(args['<args>']) == 1):
            print("INFO: Really deleting all instances ?")
            if confirm_choice() == 'c':
                print("INFO: Confirmed deleting all instances")
                try:
                    api_response_get_in_delete = api_instance.cf_manager_rest_api_get_instances(username, password, limit=args['--limit'])
                    if(len(api_response_get_in_delete) > 0):
                        for this_instance in tqdm(api_response_get_in_delete):                                  
                            # Delete an instance
                            print("INFO: Deleting instance " + str(this_instance.instance_id) + " ... ")
                            try:
                                api_instance.cf_manager_rest_api_delete_instance(username, password, this_instance.instance_id)
                            except ApiException as e_in_delete:
                                print("Exception when calling InstancesApi->cf_manager_rest_api_delete_instance: %s\n" % e_in_delete)        
                    else:
                        print("INFO: No instances to delete.")
                except ApiException as e_in_get:
                    print("Exception when calling InstancesApi->cf_manager_rest_api_get_instances: %s\n" % e_in_get)              
                    exit(-1)
            else:
                print ("INFO: Canceling deleting all instances")
        elif (len(args['<args>']) == 2):
            instance_id = args['<args>'][1]
            # Delete an instance
            print("INFO: Deleting instance " + str(instance_id) + " ... ")
            try:
                api_response = api_instance.cf_manager_rest_api_delete_instance(username, password, instance_id)
            except ApiException as e:
                print("Exception when calling InstancesApi->cf_manager_rest_api_delete_instance: %s\n" % e)
                exit(-1)
            return(api_response)
        else:
            exit(print("ERROR: invalid arguments provided in cfsp instance delete. Aborting..."))
    else:
        exit(print("ERROR: invalid command provided in cfsp instance. Type 'cfsp help instance' to get a list of supported commands. Aborting..."))
if __name__ == '__main__':
    main(args)
