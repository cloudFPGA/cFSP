# swagger_client.ClustersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cf_manager_rest_api_delete_cluster**](ClustersApi.md#cf_manager_rest_api_delete_cluster) | **DELETE** /clusters/{cluster_id} | Delete a cluster
[**cf_manager_rest_api_extend_cluster**](ClustersApi.md#cf_manager_rest_api_extend_cluster) | **PUT** /clusters/{cluster_id}/extend | Add nodes to an existing cluster
[**cf_manager_rest_api_get_cluster_single**](ClustersApi.md#cf_manager_rest_api_get_cluster_single) | **GET** /clusters/{cluster_id} | Get a cluster
[**cf_manager_rest_api_get_clusters**](ClustersApi.md#cf_manager_rest_api_get_clusters) | **GET** /clusters | Get all clusters of a user
[**cf_manager_rest_api_post_clusters**](ClustersApi.md#cf_manager_rest_api_post_clusters) | **POST** /clusters | Request a cluster
[**cf_manager_rest_api_reduce_cluster**](ClustersApi.md#cf_manager_rest_api_reduce_cluster) | **PUT** /clusters/{cluster_id}/reduce | Remove nodes from an existing cluster
[**cf_manager_rest_api_restart_cluster**](ClustersApi.md#cf_manager_rest_api_restart_cluster) | **PATCH** /clusters/{cluster_id}/restart | Restart all application on FPGAs in this cluster
[**cf_manager_rest_api_update_node_of_cluster**](ClustersApi.md#cf_manager_rest_api_update_node_of_cluster) | **PUT** /clusters/{cluster_id}/{node_id} | Reconfigure one FPGA node of an existing cluster

# **cf_manager_rest_api_delete_cluster**
> cf_manager_rest_api_delete_cluster(username, password, cluster_id)

Delete a cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClustersApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cluster_id = 56 # int | ID of a cluster

try:
    # Delete a cluster
    api_instance.cf_manager_rest_api_delete_cluster(username, password, cluster_id)
except ApiException as e:
    print("Exception when calling ClustersApi->cf_manager_rest_api_delete_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cluster_id** | **int**| ID of a cluster | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_extend_cluster**
> Cluster cf_manager_rest_api_extend_cluster(body, username, password, cluster_id, dont_verify_memory=dont_verify_memory)

Add nodes to an existing cluster

This adds nodes to an existing cluster, as specified in the parameter `cluster_details`.  **Details** on how to describe a cluster can be found at the **Implementation Notes of the `POST /clusters` API call**. All mentioned rules apply for this method as well.  After creating all new nodes, the runtime information of all nodes will be updated. The Roles of the already existing FPGA nodes are **not** reset during this method.  If errors occur during this method (e.g. 424 or 507), the original cluster will be unaffected. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClustersApi()
body = [swagger_client.ClustersBody()] # list[ClustersBody] | Mapping of Node-IDs to Images
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cluster_id = 56 # int | ID of a cluster
dont_verify_memory = 0 # int | If 1, don't verify the DDR4 memory during setup (optional) (default to 0)

try:
    # Add nodes to an existing cluster
    api_response = api_instance.cf_manager_rest_api_extend_cluster(body, username, password, cluster_id, dont_verify_memory=dont_verify_memory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->cf_manager_rest_api_extend_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ClustersBody]**](ClustersBody.md)| Mapping of Node-IDs to Images | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cluster_id** | **int**| ID of a cluster | 
 **dont_verify_memory** | **int**| If 1, don&#x27;t verify the DDR4 memory during setup | [optional] [default to 0]

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_cluster_single**
> Cluster cf_manager_rest_api_get_cluster_single(username, password, cluster_id)

Get a cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClustersApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cluster_id = 56 # int | ID of a cluster

try:
    # Get a cluster
    api_response = api_instance.cf_manager_rest_api_get_cluster_single(username, password, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->cf_manager_rest_api_get_cluster_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cluster_id** | **int**| ID of a cluster | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_clusters**
> list[Cluster] cf_manager_rest_api_get_clusters(username, password, limit=limit)

Get all clusters of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClustersApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all clusters of a user
    api_response = api_instance.cf_manager_rest_api_get_clusters(username, password, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->cf_manager_rest_api_get_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**list[Cluster]**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_clusters**
> Cluster cf_manager_rest_api_post_clusters(body, username, password, project_name=project_name, dont_verify_memory=dont_verify_memory)

Request a cluster

This triggers the configuration of all *FPGA nodes* of a cluster as specified in the parameter `cluster_details`.  The entry for an FPGA node must look like:  ```json {   \"node_id\": unique integer,   \"image_id\": \"XXX-XX-XXX\" } ```  The parameters `instance_id` and `node_ip` are set by the Resource Manager. The `node_id`s must be unique for the whole cluster (FPGAs and CPUs).   It is necessary to submit the information about the CPU nodes of a heterogeneous cluster to compile and distribute the *network routing configuration for the FPGAs correctly*.  Hence, the entry for a CPU must look like:  ```json {   \"node_id\": unique integer,   \"image_id\": \"NON_FPGA\",   \"node_ip\": \"10.12.47.11\" } ```  The setup of the CPU nodes must be done by the users themselves. The `node_ip` of a CPU must be in the OpenStack user subnetwork (i.e. `10.12.X.Y`). Currently, the maximum supported size of a cluster is 64 (FPGA + CPU nodes). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClustersApi()
body = [swagger_client.ClustersBody()] # list[ClustersBody] | Mapping of Node-IDs to Images
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
project_name = 'default' # str | Name of the OpenStack project the quota should be acounted to, if a user has multiple projects. (optional) (default to default)
dont_verify_memory = 0 # int | If 1, don't verify the DDR4 memory during setup (optional) (default to 0)

try:
    # Request a cluster
    api_response = api_instance.cf_manager_rest_api_post_clusters(body, username, password, project_name=project_name, dont_verify_memory=dont_verify_memory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->cf_manager_rest_api_post_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ClustersBody]**](ClustersBody.md)| Mapping of Node-IDs to Images | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **project_name** | **str**| Name of the OpenStack project the quota should be acounted to, if a user has multiple projects. | [optional] [default to default]
 **dont_verify_memory** | **int**| If 1, don&#x27;t verify the DDR4 memory during setup | [optional] [default to 0]

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_reduce_cluster**
> Cluster cf_manager_rest_api_reduce_cluster(body, username, password, cluster_id)

Remove nodes from an existing cluster

This remove nodes the nodes in the `nodes_to_remove` list from an existing cluster.  The `nodes_to_remove` list must contain the `node_id`s of the nodes that should be removed.  After removing all specified nodes, the runtime information of all remaining nodes will be updated. The Roles of the remaining FPGA nodes are **not** reset during this method.  If the last remaining FPGA node is removed, the complete cluster will be deleted (like `DELETE /cluster/{cluster_id}`).  If errors occur during this method, the original/remaining cluster will be unaffected. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClustersApi()
body = [56] # list[int] | List of Node-IDs that should be removed
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cluster_id = 56 # int | ID of a cluster

try:
    # Remove nodes from an existing cluster
    api_response = api_instance.cf_manager_rest_api_reduce_cluster(body, username, password, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->cf_manager_rest_api_reduce_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)| List of Node-IDs that should be removed | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cluster_id** | **int**| ID of a cluster | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_restart_cluster**
> cf_manager_rest_api_restart_cluster(username, password, cluster_id)

Restart all application on FPGAs in this cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClustersApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cluster_id = 56 # int | ID of a cluster

try:
    # Restart all application on FPGAs in this cluster
    api_instance.cf_manager_rest_api_restart_cluster(username, password, cluster_id)
except ApiException as e:
    print("Exception when calling ClustersApi->cf_manager_rest_api_restart_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cluster_id** | **int**| ID of a cluster | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_update_node_of_cluster**
> Cluster cf_manager_rest_api_update_node_of_cluster(image_id, username, password, cluster_id, node_id, dont_verify_memory=dont_verify_memory)

Reconfigure one FPGA node of an existing cluster

This method re-configures the given FPGA node in the given cluster. All settings remain the same and the runtime information of the cluster will be written to the updated instance again.  The Roles of the other FPGA nodes are **not** reset during this method.  If errors occur during this method, the other nodes of the cluster will be unaffected. **If this call fails with `507`** and the FPGA worked without any problems before, then the submitted image probably doesn't work (i.e. `507` doesn't imply a failure of the FPGA board). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClustersApi()
image_id = 'image_id_example' # str | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cluster_id = 56 # int | ID of a cluster
node_id = 56 # int | ID of a node within a cluster
dont_verify_memory = 0 # int | If 1, don't verify the DDR4 memory during setup (optional) (default to 0)

try:
    # Reconfigure one FPGA node of an existing cluster
    api_response = api_instance.cf_manager_rest_api_update_node_of_cluster(image_id, username, password, cluster_id, node_id, dont_verify_memory=dont_verify_memory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersApi->cf_manager_rest_api_update_node_of_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cluster_id** | **int**| ID of a cluster | 
 **node_id** | **int**| ID of a node within a cluster | 
 **dont_verify_memory** | **int**| If 1, don&#x27;t verify the DDR4 memory during setup | [optional] [default to 0]

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

