"""
Usage:
    cfsp user (load | show) [credentials_file]
Commands:
    load         Load credentials from a file
    show         Show the credentials of a file
"""
from docopt import docopt
import json
import cfsp_globals
import sys
#import dill


####################################################################################################
# User functions
####################################################################################################

class cFuser:
    """A user in the cloudFPGA world"""

    def __init__(self, credentials_file):
        username, password, project = load_user_credentials(credentials_file)
        self.project = project
        self.username = username
        self.password = password
        self.credentials_file = credentials_file


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
        print("File     : " + self.credentials_file)
        print("User     : " + self.username)
        print("Password : " + self.password)
        print("Project  : " + self.project)



def main(args):
    if ((len(args['<args>']) < 1) or (len(args['<args>']) > 2)):
        print("ERROR: invalid arguments provided in 'cfsp user' command. Aborting...")
        exit(print(__doc__))
    
    print(args['<args>'])
    if args['<args>'][0] == 'load':
        if (len(args['<args>']) == 2):
            user=cFuser(args['<args>'][1])
        elif (len(args['<args>']) == 1):
            user=cFuser("user.json")
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
        #dill.dump_session(cfsp_globals.__cfsp_session_file__)
    elif args['<args>'][0] == 'show':
        if (len(args['<args>']) == 2):
            user=cFuser(args['<args>'][1])
            print_user_credentials_from_file(args['<args>'][1])
        elif (len(args['<args>']) == 1):
            user=cFuser("user.json")
        else:
            print("ERROR: invalid arguments provided in cfsp user show. Aborting...")
            sys.exit(-1)
            
def load_user_credentials(json_file):
    """returns username, password, and project from a JSON file"""
    username = ""
    password = ""
    project = ""

    try:
        with open(json_file, 'r') as infile:
            data = json.load(infile)
        username = data['credentials']['username']
        password = data['credentials']['password']
        if 'project' in data:
            project = data['project']
        else:
            project = cfsp_globals.__openstack_user_template__['project']
    except Exception as e:
        print(e)
        print("Writing credentials template to {}\n".format(json_file))
        with open(json_file, 'w') as outfile:
            json.dump(cfsp_globals.__openstack_user_template__, outfile)
    #dill.dump_session('./cf_bk_dill.pkl')
    return username, password, project           
    #sys.exit(1)


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
        print("No credentials found \n")
        sys.exit(1)
        
        
        
        
if __name__ == '__main__':
    main()        
