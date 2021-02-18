#  *
#  *                       cloudFPGA
#  *     Copyright IBM Research, All Rights Reserved
#  *    =============================================
#  *     Created: Sep. 2020
#  *     Authors: FAB, WEI, NGL, DID
#  *
#  *     Description:
#  *      A test example of cF Python library.
#  *
#  *

import sys
sys.path.append("../module")
import cF

print("############# Start testing: print_usage ###############\n")
cF.print_usage()
print("############# End testing:   print_usage ###############\n\n")

print("############# Start testing: load_user_credentials ###############\n")
cF.load_user_credentials('./')
print("############# End testing:   load_user_credentials ###############\n\n")

print("############# Start testing: show_user_credentials ###############\n\n")
cF.show_user_credentials('./')
print("############# End testing:   show_user_credentials ###############\n\n")

print("############# Start testing: get_clusters_data ###############\n")
cluster_data=cF.get_clusters_data(100)
print(cluster_data)
print("############# End testing:   get_clusters_data ###############\n\n")

print("############# Start testing: post_cluster ###############\n")
cluster_data=cF.post_cluster(1, "33ffdea4-4462-48ac-9b32-77768ae95135", "10.2.0.4")
cluster_id=cluster_data['cluster_id']
print(cluster_id)
print("############# End testing:   post_cluster ###############\n\n")

print("############# Start testing: delete_cluster_data ###############\n")
cF.delete_cluster_data(cluster_id)
print("############# End testing:   delete_cluster_data ###############\n\n")
