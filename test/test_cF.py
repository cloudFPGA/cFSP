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

#cF.print_usage()

cF.load_user_credentials('./')

cF.show_user_credentials('./')

cluster_data=cF.get_clusters_data(100)
print(cluster_data)
#cluster_data=cF.post_cluster(1, "33ffdea4-4462-48ac-9b32-77768ae95135", "10.2.0.4")

#cF.delete_cluster_data(82)
