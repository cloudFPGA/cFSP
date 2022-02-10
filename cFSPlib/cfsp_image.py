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
    cfsp image (get | post | delete)    
Commands:
    get <id>     Get all images of a user. Either <id> of image or no argument for all.
    post         Request an image.
    delete id    Delete an image with image_id=id.    
"""
from __future__ import absolute_import

import sys,os
import json
python_api_client_path = os.getcwd()+"/cFSPlib/python_api_client/"
sys.path.append(python_api_client_path)

import cfsp_globals
import swagger_client
from swagger_client.api.images_api import ImagesApi  # noqa: E501
from swagger_client.rest import ApiException
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration


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
    api_instance = ImagesApi(api_client=api_client)

    if ((len(args['<args>']) < 1) or (len(args['<args>']) > 2)):
        print("ERROR: invalid arguments provided in 'cfsp image' command. Aborting...")
        exit(print(__doc__))
    
    username = cfsp_globals.__cfsp_username__
    password = cfsp_globals.__cfsp_password__
    project_name = cfsp_globals.__cfsp_project__

    if args['<args>'][0] == 'get':
        if (len(args['<args>']) == 2):
            try:
                api_response = api_instance.cf_manager_rest_api_get_image_single(username, password, args['<args>'][1])                
            except ApiException as e:
                print("Exception when calling ImagesApi->cf_manager_rest_api_get_image_single: %s\n" % e)              
                exit(-1)
        elif (len(args['<args>']) == 1):
            try:
                api_response = api_instance.cf_manager_rest_api_get_images(username, password, limit=args['--limit'])
            except ApiException as e:
                print("Exception when calling ImagesApi->cf_manager_rest_api_get_images: %s\n" % e)              
                exit(-1)            
        else:
            exit(print("ERROR: invalid arguments provided in cfsp image get. Aborting..."))
        return(api_response)
    elif args['<args>'][0] == 'post':
        try:
            # Upload an image
            image_details = '{   "breed": "SHELL",   "fpga_board": "FMKU60",   "shell_type": "Themisto",   "comment" : "Some valuable information for humans (optional)"}'
            pr_verify_rpt = ""
            image_file = args['--image_file']
            if (image_file.find("pblock") != -1):
                print("ERROR: the image file contains the keyword 'pblock' which is typically generated in pr flow. Do you wish to continue anyway ?")
                if (confirm_choice() != 'c'):
                    exit(print("ERROR: Aborting upon user selection..."))                
            length_image_file = len(image_file)
            image_file_type = image_file[length_image_file - 3 : length_image_file]
            if (image_file_type == "bit"):
                api_response = api_instance.cf_manager_rest_api_post_images(image_details, image_file, pr_verify_rpt, username, password)
                return(api_response)
            else:
                exit(print("ERROR: invalid image file provided in cfsp post-app-logic. You should provide a .bit file instead. Aborting..."))
        except ApiException as e:
            print("Exception when calling ImagesApi->cf_manager_rest_api_post_images: %s\n" % e)
            exit(-1)
    elif args['<args>'][0] == 'post-app-logic':
        try:
            image_file = args['--image_file']
            if (image_file.find("pblock") == -1):
                print("WARNING: the image file does not contain the keyword 'pblock' which is typically generated in pr flow. Do you wish to continue anyway ?")
                if (confirm_choice() != 'c'):
                    exit(print("ERROR: Aborting upon user selection..."))
            image_dirname = os.path.dirname(image_file)
            json_file = image_dirname+ "/3_topFMKU60_STATIC.json"
            print("INFO: This json file will be used: " + json_file)
            with open(json_file) as f:
                data = json.load(f)
            cl_id = str(data['id'])
            #TODO: Parse also shell, fpga_board and comment from the json file
            image_details = '{"cl_id": "' + cl_id + '", "fpga_board": "FMKU60", "shell_type": "Themisto", "comment" : "Some valuable information for humans (optional)"}'
            length_image_file = len(image_file)
            image_file_type = image_file[length_image_file - 3 : length_image_file]
            image_file_name = image_file[0 : length_image_file - 4]
            if (image_file_type == "bin"):
                sig_file = args['--sig_file']
                if (sig_file is None):
                    sig_file = image_file + ".sig"
                    print("INFO: No --sig_file provided. Assuming " + sig_file)
                pr_verify_rpt = args['--pr_verify_rpt']
                if (pr_verify_rpt is None):
                    pr_verify_rpt = image_file_name + ".rpt"
                    pr_verify_rpt_new = pr_verify_rpt.replace("4_","5_") # FIXME: This is a bug if the path, apart from the filename, contains the characters '4_'.
                    pr_verify_rpt = pr_verify_rpt_new
                    print("INFO: No --pr_verify_rpt provided. Assuming " + pr_verify_rpt)
                # Upload an image
                api_response = api_instance.cf_manager_rest_api_post_app_logic(image_details, image_file, sig_file, pr_verify_rpt, username, password)            
                return(api_response)
            else:
                exit(print("ERROR: invalid image file provided in cfsp post-app-logic. You should provide a .bin file instead. Aborting..."))
        except ApiException as e:
            print("Exception when calling ImagesApi->cf_manager_rest_api_post_app_logic: %s\n" % e)
            exit(-1)
    elif args['<args>'][0] == 'delete':
        if (len(args['<args>']) == 2):
            try:
            # Delete an image
                image_id = args['<args>'][1]
                api_instance.cf_manager_rest_api_delete_image(username, password, image_id)
            except ApiException as e:
                print("Exception when calling ImagesApi->cf_manager_rest_api_delete_image: %s\n" % e)
        else:
            exit(print("ERROR: invalid arguments provided in cfsp image delete. Aborting..."))
    else:
        exit(print("ERROR: invalid command provided in cfsp image. Type 'cfsp help image' to get a list of supported commands. Aborting..."))            

if __name__ == '__main__':
    main(args)
