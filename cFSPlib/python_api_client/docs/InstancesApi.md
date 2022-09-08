# swagger_client.InstancesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cf_manager_rest_api_app_restart_instance**](InstancesApi.md#cf_manager_rest_api_app_restart_instance) | **PATCH** /instances/{instance_id}/app_restart | Triggers app restart of this instance
[**cf_manager_rest_api_delete_instance**](InstancesApi.md#cf_manager_rest_api_delete_instance) | **DELETE** /instances/{instance_id} | Remove an instance
[**cf_manager_rest_api_get_instance**](InstancesApi.md#cf_manager_rest_api_get_instance) | **GET** /instances/{instance_id} | Get a single instance
[**cf_manager_rest_api_get_instances**](InstancesApi.md#cf_manager_rest_api_get_instances) | **GET** /instances | Get all instances of a user
[**cf_manager_rest_api_instance_api_gateway**](InstancesApi.md#cf_manager_rest_api_instance_api_gateway) | **POST** /instances/{instance_id}/api_gateway | Forwards a custom HTTP API request
[**cf_manager_rest_api_instance_change_runlevel**](InstancesApi.md#cf_manager_rest_api_instance_change_runlevel) | **POST** /instances/{instance_id}/runlevel | Changes the &#x60;runlevel&#x60; of the instance (stack developers only)
[**cf_manager_rest_api_instance_get_runlevel**](InstancesApi.md#cf_manager_rest_api_instance_get_runlevel) | **GET** /instances/{instance_id}/runlevel | Returns the current &#x60;runlevel&#x60; of the instance (stack developers only)
[**cf_manager_rest_api_post_instances**](InstancesApi.md#cf_manager_rest_api_post_instances) | **POST** /instances | Create an instance
[**cf_manager_rest_api_update_instance**](InstancesApi.md#cf_manager_rest_api_update_instance) | **PUT** /instances/{instance_id} | Reprogramm an instance

# **cf_manager_rest_api_app_restart_instance**
> cf_manager_rest_api_app_restart_instance(username, password, instance_id)

Triggers app restart of this instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier

try:
    # Triggers app restart of this instance
    api_instance.cf_manager_rest_api_app_restart_instance(username, password, instance_id)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_app_restart_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_delete_instance**
> cf_manager_rest_api_delete_instance(username, password, instance_id)

Remove an instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier

try:
    # Remove an instance
    api_instance.cf_manager_rest_api_delete_instance(username, password, instance_id)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_delete_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_instance**
> Instance cf_manager_rest_api_get_instance(username, password, instance_id)

Get a single instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier

try:
    # Get a single instance
    api_response = api_instance.cf_manager_rest_api_get_instance(username, password, instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_get_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 

### Return type

[**Instance**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_instances**
> list[Instance] cf_manager_rest_api_get_instances(username, password, limit=limit)

Get all instances of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all instances of a user
    api_response = api_instance.cf_manager_rest_api_get_instances(username, password, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_get_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**list[Instance]**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_instance_api_gateway**
> cf_manager_rest_api_instance_api_gateway(body, username, password, instance_id)

Forwards a custom HTTP API request

Forwards a custom HTTP API request to the FMC/Middleware (management interface) and returns the answer. Before forwarding the request, a filter will be applied to block unauthorized access.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
body = swagger_client.InstanceIdApiGatewayBody() # InstanceIdApiGatewayBody | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier

try:
    # Forwards a custom HTTP API request
    api_instance.cf_manager_rest_api_instance_api_gateway(body, username, password, instance_id)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_instance_api_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InstanceIdApiGatewayBody**](InstanceIdApiGatewayBody.md)|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_instance_change_runlevel**
> cf_manager_rest_api_instance_change_runlevel(new_runlevel, username, password, instance_id)

Changes the `runlevel` of the instance (stack developers only)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
new_runlevel = 56 # int | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier

try:
    # Changes the `runlevel` of the instance (stack developers only)
    api_instance.cf_manager_rest_api_instance_change_runlevel(new_runlevel, username, password, instance_id)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_instance_change_runlevel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_runlevel** | **int**|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_instance_get_runlevel**
> InlineResponse2005 cf_manager_rest_api_instance_get_runlevel(username, password, instance_id)

Returns the current `runlevel` of the instance (stack developers only)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier

try:
    # Returns the current `runlevel` of the instance (stack developers only)
    api_response = api_instance.cf_manager_rest_api_instance_get_runlevel(username, password, instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_instance_get_runlevel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_instances**
> InlineResponse2001 cf_manager_rest_api_post_instances(image_id, username, password, project_name=project_name, dont_verify_memory=dont_verify_memory)

Create an instance

This configures an FPGA of type `fpga_board` (from the image metadata) with the given image and sets up the network accordingly.  Please contact the administrators, if this request failed several times with `500` or `507`.  If a user belongs to multiple projects, the Quota of the first project (in alphabetical order) is used. If another Quota should be used, the parameter `project_name` must be set accordingly.  If the given image is a partial bitstream, the partial reconfiguration flow is applied automatically (`breed` is `\"ROLE\"`). In that case, this request tries to find a resource with the corresponding `shell_type` as defined by the image. If no board with the requested `shell_type` is available, one board gets configured with the newest `shell_type` SHELL image. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
image_id = 'image_id_example' # str | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
project_name = 'default' # str | Name of the OpenStack project the quota should be acounted to, if a user has multiple projects. (optional) (default to default)
dont_verify_memory = 0 # int | If 1, don't verify the DDR4 memory during setup (optional) (default to 0)

try:
    # Create an instance
    api_response = api_instance.cf_manager_rest_api_post_instances(image_id, username, password, project_name=project_name, dont_verify_memory=dont_verify_memory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_post_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **project_name** | **str**| Name of the OpenStack project the quota should be acounted to, if a user has multiple projects. | [optional] [default to default]
 **dont_verify_memory** | **int**| If 1, don&#x27;t verify the DDR4 memory during setup | [optional] [default to 0]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_update_instance**
> InlineResponse2001 cf_manager_rest_api_update_instance(image_id, username, password, instance_id, dont_verify_memory=dont_verify_memory)

Reprogramm an instance

Reprogram an instance with the submitted image and configure all current settings again afterwards. Hence, this call reuses the same FPGA again (in opposition to DELETE and POST again). This is **intended only for single instances**, not to update one instance out of a cluster.  **If this call fails with `507`** and the FPGA worked without any problems before, then the submitted image probably doesn't work (i.e. `507` doesn't imply a failure of the FPGA board). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstancesApi()
image_id = 'image_id_example' # str | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier
dont_verify_memory = 0 # int | If 1, don't verify the DDR4 memory during setup (optional) (default to 0)

try:
    # Reprogramm an instance
    api_response = api_instance.cf_manager_rest_api_update_instance(image_id, username, password, instance_id, dont_verify_memory=dont_verify_memory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancesApi->cf_manager_rest_api_update_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 
 **dont_verify_memory** | **int**| If 1, don&#x27;t verify the DDR4 memory during setup | [optional] [default to 0]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

