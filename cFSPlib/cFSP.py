# /*******************************************************************************
#  * Copyright 2016 -- 2022 IBM Corporation
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *     http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
# *******************************************************************************/

#  *
#  *                       cloudFPGA
#  *    =============================================
#  *     Created: Apr 2019
#  *     Authors: FAB, WEI, NGL, DID
#  *
#  *     Description:
#  *       Python tool to interact with cFRM.
#  *

# @file       cFSP.py
# @brief      This is the main file of cFSP
# @author     DID
# @date       Dec 2021
# @ingroup cFSP
# @addtogroup cFSP
# \{

#! /usr/bin/env python
"""cfsp.

cloudFPGA Support Package (cfsp)
cfsp is a command-line tool that helps a cloudFPGA user to work with cloudFPGA Resource Manager (cFRM).
Usage: 
    cfsp    [-c CFGFILE] [--version] [--help] [--username=<username>] [--password=<password>] [--project=<project>]
            [--image_id=<image_id>]...
            [--node_ip=<node_ip>]...
            [--node_id=<node_id>]...
            [--cluster_id=<cluster_id>]
            [--image_file=<image_file>] [--sig_file=<sig_file>] [--pr_verify_rpt=<pr_verify_rpt] [--dont_verify_memory=<dont_verify_memory>]
            [--limit=<limit>] [--repeat=<repeat>]
            [<command>] [<args>...]

Commands:
    user            Adding or showing the credentials of a user.
    cluster         Creating, showing and deleting clusters.
    image           Uploading, showing and deleting FPGA images.
    instance        Creating, showing and deleting instances.

Options:
    -h --help            Show this screen.
    -v --version         Show version.
    -c --config CFGFILE  Specify the configfile that rsnapshot should use 
                         [default: ./user.json]
    --username=<username>       Your ZYC2 username [default: username_example].
    --password=<password>       Your ZYC2 password [default: password_example].
    --project=<password>        The user's project [default: project_example].
    --image_id=<image_id>       The id of the uploaded FPGA image, or NON_FPGA for a CPU VM node.
    --node_ip=<node_ip>         The ip of the user's VM, e.g. a ZYC2 VM.
    --node_id=<node_id>         The id (rank) of either the VPN user's VM or FPGAs.
    --cluster_id=<cluster_id>   The id of a cluster to update or extend.
    --image_file=<image_file>      The FPGA image file to be uploaded [default: ./image.bit].
    --sig_file=<sig_file>          An FPGA bitstream signature file containing hashes from the build process.
    --pr_verify_rpt=<pr_verify_rpt An FPGA report containing the output of the automatically run pr_verify command.
    --dont_verify_memory=<dont_verify_memory>   If 1, don't verify the DDR4 memory during setup [default: 0].
    --limit=<limit>             The limit of get for clusters, images, instances [default: 100].
    --repeat=<repeat>           The numper of times to repeat the command [default: 1].
    
See 'cfsp help <command>' for more information on a specific command.

Copyright IBM Research, licensed under the Apache License 2.0.

"""

from __future__ import print_function, unicode_literals

import json
import os
import sys
from docopt import docopt
import re
from PyInquirer import prompt, print_json
from pprint import pprint
from tqdm import tqdm

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import cfsp_globals
import cfsp_user
import cfsp_cluster
import cfsp_image
import cfsp_instance

from util import print_usage
import mngmt
import comm


version_path = os.path.dirname(os.path.abspath(__file__))+"/version.txt"
with open(version_path,"r") as fh:
    for line in fh:
        __version__ = line.rstrip("\n")
fh.close()

# This variable check weather we call cfsp a script from the command line, 
# or as module from another Python file.
is_script = False

def check_credentials(CFGFILE):
    #if os.path.isfile(cfsp_globals.__cfsp_session_file__):
    #    dill.load_session(cfsp_globals.__cfsp_session_file__)
    #else:
    args = docopt(__doc__, version=__version__)
    args['<args>'] = ['load']
    cfsp_user.main(args)
    
def main(args):

    argv = [args['<command>']] + args['<args>']
    #print(args['<args>'])
    #print([args['<command>']] + args['<args>'])

    for repeat_id in tqdm(range(0,int(args['--repeat']))):
        cfrm_response = ''
        print("INFO: Repeat #"+str(repeat_id))
        if args['<command>'] == 'user':
            cfsp_user.main(args)
        elif args['<command>'] == 'cluster':
            check_credentials(args['--config'])
            cfrm_response=cfsp_cluster.main(args)
        elif args['<command>'] == 'image':
            check_credentials(args['--config'])
            cfrm_response=cfsp_image.main(args)
        elif args['<command>'] == 'instance':
            check_credentials(args['--config'])
            cfrm_response=cfsp_instance.main(args)
        elif args['<command>'] in ['help', None]:
            if args['<args>'] == ['user']:
                print("docopt user")
                print(docopt(cfsp_user.__doc__, argv=argv))
            elif args['<args>'] == ['cluster']:
                print(docopt(cfsp_cluster.__doc__, argv=argv))
            elif args['<args>'] == ['image']:
                print(docopt(cfsp_image.__doc__, argv=argv))
            elif args['<args>'] == ['instance']:
                print(docopt(cfsp_instance.__doc__, argv=argv))
            else:
                print(docopt(__doc__, version=__version__))
        else:
            print("ERROR: unknown command. Aborting...")
            exit(print(docopt(__doc__, version=__version__)))
            
        if (is_script):
            pprint(cfrm_response)
        else:
            return(cfrm_response)


if __name__ == '__main__':
    if not (hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)):
        # This works with virtualenv for Python 3 and 2 and also for the venv module in Python 3
        print("ERROR: It looks like this cFSP isn't running in a virtual environment. Aborting.")
        sys.exit(1)
        
    args = docopt(__doc__, version=__version__)
    is_script = True
    main(args)
    exit(0)


# ! \} 
