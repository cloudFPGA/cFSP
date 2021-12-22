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
#  *      A test example of cFSP Python library.
#  *
#  *

# make sure cFPY's root folder is in the PYTHONPATH, or add a line as below
import sys
sys.path.append("../")

import cFSPlib

retval=0
num_tests=10

print("############# Start testing: print_usage ###############\n")
cFSPlib.util.print_usage()
print("############# End testing:   print_usage ###############\n\n")

####################################################################################################
# Test User functions
####################################################################################################

print("############# Start testing: load_user_credentials ###############\n")
my_user = cFSPlib.mngmt.cFuser("./user_example.json")
retval=retval+1
print("############# End testing:   load_user_credentials ###############\n\n")

print("############# Start testing: show_user_credentials ###############\n\n")
my_user.print_credentials()
retval=retval+1
print("############# End testing:   show_user_credentials ###############\n\n")


####################################################################################################
# Test Cluster functions
####################################################################################################

print("############# Start testing: post_cluster ###############\n")
my_cluster = cFSPlib.mngmt.post_cluster(my_user, 1, "33ffdea4-4462-48ac-9b32-77768ae95135", "10.2.0.4")
if type(my_cluster) is cFSPlib.mngmt.cFcluster:
    cluster_id = my_cluster.id
    print(my_cluster)
    retval=retval+1
else:
    print("Failed to create cluster")
    cluster_id = None
print("############# End testing:   post_cluster ###############\n\n")

print("############# Start testing: get_clusters_data ###############\n")
clusters_data = cFSPlib.mngmt.get_clusters_data(my_user, 100)
print(clusters_data)
retval=retval+1
print("############# End testing:   get_clusters_data ###############\n\n")

print("############# Start testing: get_cluster_data ###############\n")
if (len(clusters_data) != 0):
    first_cluster = cFSPlib.mngmt.cFcluster(my_user, clusters_data[0])
    cluster_data = cFSPlib.mngmt.get_cluster_data(first_cluster)
    print(cluster_data)
    retval=retval+1
else:
    print("WARNING: No cluster to get.")
print("############# End testing:   get_cluster_data ###############\n\n")

print("############# Start testing: restart_cluster_apps ###############\n")
if "first_cluster" in globals():
    cFSPlib.mngmt.restart_cluster_apps(first_cluster)
    retval=retval+1
else:
    print("WARNING: No cluster to restart.")    
print("############# End testing:   restart_cluster_apps ###############\n\n")


####################################################################################################
# Test Instances functions
####################################################################################################

print("############# Start testing: get_instances_data ###############\n")
instances_data = cFSPlib.mngmt.get_instances_data(my_user, 100)
print(instances_data)
retval=retval+1
print("############# End testing:   get_instances_data ###############\n\n")

print("############# Start testing: get_instance_data ###############\n")
if (len(instances_data) != 0):
    first_instance = cFSPlib.mngmt.cFinstance(my_user, instances_data[0])
    instance_data = cFSPlib.mngmt.get_instance_data(first_instance)
    print(instance_data)
    retval=retval+1
else:
    print("WARNING: No Instance to get.")
print("############# End testing:   get_instance_data ###############\n\n")

print("############# Start testing: restart_instance_data ###############\n")
if "first_instance" in globals():
    cFSPlib.mngmt.restart_instance_app(first_instance)
    retval=retval+1
else:
    print("WARNING: No instance to restart.")
print("############# End testing:   restart_instance_data ###############\n\n")

####################################################################################################
# Test Images functions
####################################################################################################
## TODO



####################################################################################################
# Clean up
####################################################################################################

print("############# Start testing: delete_cluster_data ###############\n")
if type(my_cluster) is cFSPlib.mngmt.cFcluster:
    cFSPlib.mngmt.delete_cluster_data(my_cluster)
    retval=retval+1
print("############# End testing:   delete_cluster_data ###############\n\n")


####################################################################################################
# Retunrn success or fail
####################################################################################################
if (retval==num_tests):
    exit(0)
else:
    exit(-1)
         
