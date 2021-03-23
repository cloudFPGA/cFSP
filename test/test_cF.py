# /*******************************************************************************
#  * Copyright 2016 -- 2020 IBM Corporation
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
#  *      A test example of cFPy Python library.
#  *
#  *

import sys
sys.path.append("../module")
import cFPy

print("############# Start testing: print_usage ###############\n")
cFPy.print_usage()
print("############# End testing:   print_usage ###############\n\n")

print("############# Start testing: load_user_credentials ###############\n")
#cFPy.load_user_credentials('./')
my_user = cFPy.mngmt.cFuser("./user_example.json")
print("############# End testing:   load_user_credentials ###############\n\n")

print("############# Start testing: show_user_credentials ###############\n\n")
cFPy.show_user_credentials('./')
print("############# End testing:   show_user_credentials ###############\n\n")

print("############# Start testing: get_clusters_data ###############\n")
cluster_data=cFPy.get_clusters_data(100)
print(cluster_data)
print("############# End testing:   get_clusters_data ###############\n\n")

print("############# Start testing: post_cluster ###############\n")
cluster_data=cFPy.post_cluster(1, "33ffdea4-4462-48ac-9b32-77768ae95135", "10.2.0.4")
cluster_id=cluster_data['cluster_id']
print(cluster_id)
print("############# End testing:   post_cluster ###############\n\n")

print("############# Start testing: delete_cluster_data ###############\n")
cFPy.delete_cluster_data(cluster_id)
print("############# End testing:   delete_cluster_data ###############\n\n")
