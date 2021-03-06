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
#  *     Copyright IBM Research, All Rights Reserved
#  *    =============================================
#  *     Created: Mar. 2021
#  *     Authors: FAB, WEI, NGL, DID
#  *
#  *     Description:
#  *      A Python library with functions for accessing cFRM and create/delete images, instances, clusters etc.
#  *
#  *

import os
import sys
import requests
import json
import time
import datetime

from mngmt import cFuser, cFcluster

CF_DEFAULT_PORT = 2718


def send(cluster: cFcluster, node_id, data_obj, proto='udp', port=CF_DEFAULT_PORT):
    print("NOT YET IMPLEMENTED")
    return -1


def recv(cluster: cFcluster, node_id, data_obj, proto='udp', port=CF_DEFAULT_PORT):
    print("NOT YET IMPLEMENTED")
    return -1

