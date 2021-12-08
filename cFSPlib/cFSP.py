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
#  *       Python framework to create new cloudFPGA projects (cFp).
#  *

from __future__ import print_function, unicode_literals

import json
import os
import sys
from docopt import docopt
import re
from PyInquirer import prompt, print_json
from pprint import pprint

#import sys
#sys.path.append("./")

from util import print_usage
import mngmt
import comm

__version__ = 0.1

docstr = """cloudFPGA Support Package
cfsp is a command-line tool that helps a cloudFPGA user to work with cloudFPGA Resource Manager (cFRM).
Usage: 
    cfsp new (--cfdk-version=<cfdkv> | --cfdk-zip=<path-to-zip>)  [--git-url=<git-url>] [--git-init] <path-to-project-folder>
    cfsp update  <path-to-project-folder>
    cfsp upgrade (--cfdk-version=<cfdkv> | --cfdk-zip=<path-to-zip>)  [--git-url=<git-url>] <path-to-project-folder>
    cfsp adorn (--cfa-repo=<cfagit> | --cfa-zip=<path-to-zip>) <folder-name-for-addon> <path-to-project-folder>
    
    cfsp -h|--help
    cfsp -v|--version
Commands:
    new             Creates a new cFp based on the given cFDK
    update          Update the environment setting of an existing cFp
    upgrade         Upgrades the cFDK and the environment setting an existing cFp
    adorn           Installs a cloudFPGA addon (cFa) to an existing cFp
Options:
    -h --help       Show this screen.
    -v --version    Show version.
    
    --cfdk-version=<cfdkv>      Specifies that the cFDK can be accessed via Github and with cFDK-version should be used.
                                'latest' will use the latest available version.
    --git-url=<git-url>         Uses the given URL to clone cFDK instead the default.
    --cfdk-zip=<path-to-zip>    If the cFDK can't be reached via Github, a zip can be used.
    --git-init                  Creates the new cFp as git-repo; Adds the cFDK as git submodule, if not using a cfdk-zip
    --cfa-repo=<cfagit>         Link to the cFa git repository
    --cfa-zip=<path-to-zip>     Path to a cFa zip folder
Copyright IBM Research, licensed under the Apache License 2.0.
Contact: {ngl,fab,wei,did,hle}@zurich.ibm.com
"""

def main():
    arguments = docopt(docstr, version=__version__)
    print("OK")


if __name__ == '__main__':
    if not (hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)):
        # This works with virtualenv for Python 3 and 2 and also for the venv module in Python 3
        print("ERROR: It looks like this cFSP isn't running in a virtual environment. Aborting.")
        sys.exit(1)
    main()
    exit(0)
