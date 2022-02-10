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
    cfsp user (load | show) [-c CFGFILE]

commands:
    load         Load credentials from a file
    show         Show the credentials of a file

options:
    -c --config CFGFILE  Specify the configfile that rsnapshot should use 
                         [default: ./user.json]    
"""
from docopt import docopt
import json
import cfsp_globals
import sys
import os

####################################################################################################
# User functions
####################################################################################################

class cFuser:
    """A user in the cloudFPGA world"""

    def __init__(self, CFGFILE):
        username, password, project = load_user_credentials(CFGFILE)
        self.project = project
        self.username = username
        self.password = password
        self.CFGFILE = CFGFILE


    def get_auth_string(self, with_project=False):
        if with_project:
            s = "username={0}&password={1}&project_name={2}".format(self.username, self.password, self.project)
            return requests.utils.requote_uri(s)
        else:
            s = "username={0}&password={1}".format(self.username, self.password)
            return requests.utils.requote_uri(s)

    def set_project(self, new_project):
        """
        This method should be used if the cloudFPGA quota name that should be used for this handle is different from the
        default or credentials file
        :param new_project:
        :return: nothing
        """
        self.project = new_project

    def print_credentials(self):
        print("File     : " + self.CFGFILE)
        print("User     : " + self.username)
        print("Password : " + self.password)
        print("Project  : " + self.project)



def main(args):
    if (len(args['<args>']) != 1):
        print("ERROR: invalid arguments provided in 'cfsp user' command. Aborting...")
        exit(print(__doc__))
    
    if args['<args>'][0] == 'load':
        if (len(args['<args>']) == 1):
            user=cFuser(args['--config'])
        else:
            print("ERROR: invalid arguments provided in cfsp user load. Aborting...")
            sys.exit(-1)
        if args['--username'] != 'username_example':
            cfsp_globals.__cfsp_username__ = user.username = args['--username']
        else:
            cfsp_globals.__cfsp_username__ = user.username
        if args['--password'] != 'password_example':
            cfsp_globals.__cfsp_password__ = user.password = args['--password']        
        else:
            cfsp_globals.__cfsp_password__ = user.password
        if args['--project'] != 'project_example':
            cfsp_globals.__cfsp_project__ = user.project = args['--project']        
        else:
            cfsp_globals.__cfsp_project__ = user.project
        write_user_credentials(args['--config'])
    elif args['<args>'][0] == 'show':
        if (len(args['<args>']) == 1):
            print_user_credentials_from_file(args['--config'])
        else:
            print("ERROR: invalid arguments provided in cfsp user show. Aborting...")
            sys.exit(-1)
    else:
        exit(print("ERROR: invalid command provided in cfsp user. Type 'cfsp help user' to get a list of supported commands. Aborting..."))
        
def load_user_credentials(json_file):
    """returns username, password, and project from a JSON file"""
    username = ""
    password = ""
    project = ""

    try:
        if os.path.exists(json_file):
            with open(json_file, 'r') as infile:
                data = json.load(infile)
            username = data['credentials']['username']
            password = data['credentials']['password']
            if 'project' in data:
                project = data['project']
            else:
                project = cfsp_globals.__openstack_user_template__['project']
        else:
            print("INFO: Creating new user credentials file : {}\n".format(os.path.abspath(json_file)))
            write_user_credentials(json_file)
    except Exception as e:
        exit(print(e))
    return username, password, project           


def write_user_credentials(json_file):
    """writes credentials to a JSON file"""
    __cfsp_template__ = {}
    __cfsp_template__['credentials'] = {}
    __cfsp_template__['credentials']['username'] = cfsp_globals.__cfsp_username__
    __cfsp_template__['credentials']['password'] = cfsp_globals.__cfsp_password__
    __cfsp_template__['project'] = cfsp_globals.__cfsp_project__    
    try:
        with open(json_file, 'w') as outfile:
            json.dump(__cfsp_template__, outfile)
    except Exception as e:
        print(e)
        
def print_user_credentials_from_file(json_file):
    try:
        with open(json_file, 'r') as infile:
            data = json.load(infile)
        username = data['credentials']['username']
        password = data['credentials']['password']
        if 'project' in data:
            project = data['project']
        else:
            project = cfsp_globals.__openstack_user_template__['project']
        print("User     : " + username)
        print("Password : " + password)
        print("Project  : " + project)
        return 0
    except Exception as e:
        print(e)
        print("No credentials file found : "+ json_file)
        sys.exit(1)
        
        
        
        
if __name__ == '__main__':
    main()        
