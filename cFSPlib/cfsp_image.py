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
python_api_client_path = os.getcwd()+"/cFSPlib/python_api_client/"
sys.path.append(python_api_client_path)

import cfsp_globals
import swagger_client
from swagger_client.api.images_api import ImagesApi  # noqa: E501
from swagger_client.rest import ApiException
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from pprint import pprint

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
        pprint(api_response)
    elif args['<args>'][0] == 'post':
        try:
            # Upload an image
            image_details = '{   "breed": "SHELL",   "fpga_board": "FMKU60",   "shell_type": "Themisto",   "comment" : "Some valuable information for humans (optional)"}'
            pr_verify_rpt = ""
            image_file = args['--image_file']
            api_response = api_instance.cf_manager_rest_api_post_images(image_details, image_file, pr_verify_rpt, username, password)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ImagesApi->cf_manager_rest_api_post_images: %s\n" % e)
            exit(-1)
    elif args['<args>'][0] == 'delete':
        if (len(args['<args>']) == 2):
            try:
            # Delete a cluster
                image_id = args['<args>'][1]
                api_instance.cf_manager_rest_api_delete_image(username, password, image_id)
            except ApiException as e:
                print("Exception when calling ImagesApi->cf_manager_rest_api_delete_image: %s\n" % e)
        else:
            exit(print("ERROR: invalid arguments provided in cfsp image delete. Aborting..."))

if __name__ == '__main__':
    main(args)
