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
#  *     Created: Sep. 2020
#  *     Authors: FAB, WEI, NGL, DID
#  *
#  *     Description:
#  *      A test example of cFSP Python module.
#  *
#  *

import sys
from docopt import docopt

# make sure cFSPlib's folder is in the PYTHONPATH, or add a line as below
sys.path.append("../")

from cFSPlib import cFSP

retval=0
num_tests=12

# Create a variable of class cFSP docopt.
# This variable will be populated with the options we need to pass to the callable cFSP module
args=docopt(cFSP.__doc__)



####################################################################################################
# Test Help functions
####################################################################################################
print("############# Start testing: help      ###############\n")
args['<command>'] = 'help'
args['<args>'] = ['']
cFSP.main(args)
retval=retval+1
print("############# End testing:   help      ###############\n\n")



####################################################################################################
# Test User functions
####################################################################################################
print("############# Start testing: user load ###############\n")
args['<command>'] = 'user'
args['<args>'] = ['load']
cFSP.main(args)
retval=retval+1
print("############# End testing:   user load ###############\n\n")

print("############# Start testing: user show ###############\n")
args['<command>'] = 'user'
args['<args>'] = ['show']
cFSP.main(args)
retval=retval+1
print("############# End testing:   user show ###############\n\n")



####################################################################################################
# Test Instance functions
####################################################################################################
print("############# Start testing: get instance ###############\n")
args['<command>'] = 'instance'
args['<args>'] = ['get']
cfrm_response=cFSP.main(args)
print(cfrm_response)
retval=retval+1
print("############# End testing:   get instance ###############\n\n")

print("############# Start testing: post instance ###############\n")
args['<command>'] = 'instance'
args['<args>'] = ['post']
args['--image_id'] = ['74462cd5-20e3-4228-a47d-258b7e5e583a']
cfrm_response=cFSP.main(args)
print(cfrm_response)
print("INFO: The new instance has id : " + str(cfrm_response.instance_id))
retval=retval+1
print("############# End testing:   post instance ###############\n\n")

print("############# Start testing: delete instance ###############\n")
args['<command>'] = 'instance'
args['<args>'] = ['delete', str(cfrm_response.instance_id)]
cfrm_response=cFSP.main(args)
print(cfrm_response)
retval=retval+1
print("############# End testing: delete instance ###############\n\n")



####################################################################################################
# Test Image functions
####################################################################################################
print("############# Start testing: get image ###############\n")
args['<command>'] = 'image'
args['<args>'] = ['get']
cfrm_response=cFSP.main(args)
print(cfrm_response)
retval=retval+1
print("############# End testing:   get image ###############\n\n")

print("############# Start testing: post image ###############\n")
args['<command>'] = 'image'
args['<args>'] = ['post']
args['--image_file'] = './4_topFMKU60_impl_monolithic.bit'  # ensure this file exists
cfrm_response=cFSP.main(args)
print(cfrm_response)
print("INFO: The uploaded image has id : " + str(cfrm_response.id))
retval=retval+1
print("############# End testing:   post image ###############\n\n")

print("############# Start testing: delete image ###############\n")
args['<command>'] = 'image'
args['<args>'] = ['delete', str(cfrm_response.id)]
cfrm_response=cFSP.main(args)
print(cfrm_response)
retval=retval+1
print("############# End testing: delete image ###############\n\n")



####################################################################################################
# Test Cluster functions
####################################################################################################
print("############# Start testing: get cluster ###############\n")
args['<command>'] = 'cluster'
args['<args>'] = ['get']
cfrm_response=cFSP.main(args)
print(cfrm_response)
retval=retval+1
print("############# End testing:   get cluster ###############\n\n")

print("############# Start testing: post_cluster ###############\n")
args['<command>'] = 'cluster'
args['<args>'] = ['post']
args['--image_id'] = ['74462cd5-20e3-4228-a47d-258b7e5e583a']
args['--node_ip'] = ['10.12.2.100']
cfrm_response=cFSP.main(args)
print(cfrm_response)
print("INFO: The new cluster has id : " + str(cfrm_response.cluster_id))
retval=retval+1
print("############# End testing:   post_cluster ###############\n\n")

print("############# Start testing: delete cluster ###############\n")
args['<command>'] = 'cluster'
args['<args>'] = ['delete', str(cfrm_response.cluster_id)]
cfrm_response=cFSP.main(args)
print(cfrm_response)
retval=retval+1
print("############# End testing: delete cluster ###############\n\n")



####################################################################################################
# Retunrn success or fail
####################################################################################################
if (retval==num_tests):
    print("INFO: Succesfully completed " + str(num_tests) + " tests!")
    exit(0)
else:
    print("ERROR: Only " + str(retval) + " tests out of " + str(num_tests) + " completed succesfully.")
    exit(-1)
         
