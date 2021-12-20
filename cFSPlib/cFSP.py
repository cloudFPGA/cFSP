# /*******************************************************************************
#  * Copyright 2016 -- 2021 IBM Corporation
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

#! /usr/bin/env python

"""
cloudFPGA Support Package (cfsp)
cfsp is a command-line tool that helps a cloudFPGA user to work with cloudFPGA Resource Manager (cFRM).
Usage: 
    cfsp    [-c CFGFILE] [--version] [--help] [--username=<username>] [--password=<password>] [--project=<project>]
            [--image_id=<image_id>] [--node_ip=<node_ip>]
            <command> [<args>...]
    
Commands:
    user            Creates a new cFp based on the given cFDK
    cluster         Update the environment setting of an existing cFp
    image           Upgrades the cFDK and the environment setting an existing cFp
    instance        Installs a cloudFPGA addon (cFa) to an existing cFp

Options:
    -h --help            Show this screen.
    -v --version         Show version.
    -c --config CFGFILE  Specify the configfile that rsnapshot should use 
                         [default: ./user.json]
    --username=<username>       Your ZYC2 username [default: username_example].
    --password=<password>       Your ZYC2 password [default: password_example].
    --project=<password>        The user's project [default: project_example].
    
    --image_id=<image_id>       The id of the uploaded FPGA image, or NON_FPGA for a CPU VM node [default: NON_FPGA].
    --node_ip=<node_ip>         The ip of the OpenVPN user's VM, e.g. a ZYC2 VM [default: 10.12.2.100].
    
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

import cfsp_globals
#import dill
import cfsp_user
import cfsp_cluster

from util import print_usage
import mngmt
import comm

__version__ = 0.1

def check_credentials(CFGFILE):
    #if os.path.isfile(cfsp_globals.__cfsp_session_file__):
    #    dill.load_session(cfsp_globals.__cfsp_session_file__)
    #else:
    args = docopt(__doc__, version=__version__)
    args['<args>'] = ['load', CFGFILE]
    #args['--username'] = 'did'
    cfsp_user.main(args)
    
def main():
    args = docopt(__doc__, version=__version__)
    
    #print('global arguments:')
    #print(args)
    #print('command arguments:')
    
    argv = [args['<command>']] + args['<args>']
    #print("OK")

    if args['<command>'] == 'user':
        print("is user")
        cfsp_user.main(args)
        print(args['<args>'])
    elif args['<command>'] == 'cluster':
        print("is cluster")
        check_credentials(args['--config'])
        cfsp_cluster.main(args)

        
    elif args['<command>'] in ['help', None]:
        if args['<args>'] == ['user']:
            print(docopt(cfsp_user.__doc__, argv=argv))
        elif args['<args>'] == ['cluster']:
            print(docopt(cfsp_cluster.__doc__, argv=argv))
        else:
            exit(print(docopt(__doc__, version=__version__)))
        


if __name__ == '__main__':
    if not (hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)):
        # This works with virtualenv for Python 3 and 2 and also for the venv module in Python 3
        print("ERROR: It looks like this cFSP isn't running in a virtual environment. Aborting.")
        sys.exit(1)
        
    
    main()
    exit(0)
