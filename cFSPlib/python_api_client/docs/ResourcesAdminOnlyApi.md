# swagger_client.ResourcesAdminOnlyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cf_manager_rest_api_delete_resource**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_delete_resource) | **DELETE** /resources/{resource_id} | Remove a resource
[**cf_manager_rest_api_get_available_resources**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_get_available_resources) | **GET** /resources/status/{status} | Get all cloudFPGA resources in state &#x60;{status}&#x60;
[**cf_manager_rest_api_get_resources**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_get_resources) | **GET** /resources | Get all cloudFPGA resources
[**cf_manager_rest_api_get_resources_of_sled_status**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_get_resources_of_sled_status) | **GET** /resources/sled/{sled_ip}/status/ | Get status of **all resources** from a specific sled
[**cf_manager_rest_api_get_resources_of_sled_status_in_state**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_get_resources_of_sled_status_in_state) | **GET** /resources/sled/{sled_ip}/{status}/ | Get status of **all resources** from a specific sled in a specific &#x60;{status}&#x60;
[**cf_manager_rest_api_get_single_resource**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_get_single_resource) | **GET** /resources/{resource_id} | Get details of one resource
[**cf_manager_rest_api_get_single_resource_status**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_get_single_resource_status) | **GET** /resources/{resource_id}/status/ | Get status of one resource
[**cf_manager_rest_api_post_resources**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_post_resources) | **POST** /resources | Create a cloudFPGA resource
[**cf_manager_rest_api_put_resource**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_put_resource) | **PUT** /resources/{resource_id} | Update a resource
[**cf_manager_rest_api_put_resource_status**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_put_resource_status) | **PUT** /resources/{resource_id}/status/ | Update status of a resource
[**cf_manager_rest_api_put_resources_of_sled_status**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_put_resources_of_sled_status) | **PUT** /resources/sled/{sled_ip}/status/ | Update status of **all resources** from a specific sled
[**cf_manager_rest_api_put_resources_of_sled_status_in_state**](ResourcesAdminOnlyApi.md#cf_manager_rest_api_put_resources_of_sled_status_in_state) | **PUT** /resources/sled/{sled_ip}/{status}/ | Update status of **all resources** from a specific sled in a specific &#x60;{status}&#x60;

# **cf_manager_rest_api_delete_resource**
> cf_manager_rest_api_delete_resource(username, password, resource_id)

Remove a resource

Please Note, after the deletion of a resource, the freed resource-id will be assigned again for new resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
resource_id = 'resource_id_example' # str | cloudFPGA resource unique identifier

try:
    # Remove a resource
    api_instance.cf_manager_rest_api_delete_resource(username, password, resource_id)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **resource_id** | **str**| cloudFPGA resource unique identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_available_resources**
> list[Resource] cf_manager_rest_api_get_available_resources(username, password, status, limit=limit)

Get all cloudFPGA resources in state `{status}`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
status = 'status_example' # str | Status of the requested resources
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all cloudFPGA resources in state `{status}`
    api_response = api_instance.cf_manager_rest_api_get_available_resources(username, password, status, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_get_available_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **status** | **str**| Status of the requested resources | 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**list[Resource]**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_resources**
> list[Resource] cf_manager_rest_api_get_resources(username, password, limit=limit)

Get all cloudFPGA resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all cloudFPGA resources
    api_response = api_instance.cf_manager_rest_api_get_resources(username, password, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_get_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**list[Resource]**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_resources_of_sled_status**
> cf_manager_rest_api_get_resources_of_sled_status(username, password, sled_ip)

Get status of **all resources** from a specific sled

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
sled_ip = 'sled_ip_example' # str | The ip address of a SM

try:
    # Get status of **all resources** from a specific sled
    api_instance.cf_manager_rest_api_get_resources_of_sled_status(username, password, sled_ip)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_get_resources_of_sled_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **sled_ip** | **str**| The ip address of a SM | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_resources_of_sled_status_in_state**
> cf_manager_rest_api_get_resources_of_sled_status_in_state(username, password, sled_ip, status)

Get status of **all resources** from a specific sled in a specific `{status}`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
sled_ip = 'sled_ip_example' # str | The ip address of a SM
status = 'status_example' # str | Status of the requested resources

try:
    # Get status of **all resources** from a specific sled in a specific `{status}`
    api_instance.cf_manager_rest_api_get_resources_of_sled_status_in_state(username, password, sled_ip, status)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_get_resources_of_sled_status_in_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **sled_ip** | **str**| The ip address of a SM | 
 **status** | **str**| Status of the requested resources | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_single_resource**
> Resource cf_manager_rest_api_get_single_resource(username, password, resource_id)

Get details of one resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
resource_id = 'resource_id_example' # str | cloudFPGA resource unique identifier

try:
    # Get details of one resource
    api_response = api_instance.cf_manager_rest_api_get_single_resource(username, password, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_get_single_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **resource_id** | **str**| cloudFPGA resource unique identifier | 

### Return type

[**Resource**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_single_resource_status**
> InlineResponse2005 cf_manager_rest_api_get_single_resource_status(username, password, resource_id)

Get status of one resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
resource_id = 'resource_id_example' # str | cloudFPGA resource unique identifier

try:
    # Get status of one resource
    api_response = api_instance.cf_manager_rest_api_get_single_resource_status(username, password, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_get_single_resource_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **resource_id** | **str**| cloudFPGA resource unique identifier | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_resources**
> cf_manager_rest_api_post_resources(username, password, body=body)

Create a cloudFPGA resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
body = swagger_client.Resource() # Resource |  (optional)

try:
    # Create a cloudFPGA resource
    api_instance.cf_manager_rest_api_post_resources(username, password, body=body)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_post_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **body** | [**Resource**](Resource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_put_resource**
> cf_manager_rest_api_put_resource(username, password, resource_id, body=body)

Update a resource

Only the properties to update must be part of the `resource_data` field. All not mentioned properties will stay the same. It is not possible to change the `state` with this API call. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
resource_id = 'resource_id_example' # str | cloudFPGA resource unique identifier
body = swagger_client.Resource() # Resource |  (optional)

try:
    # Update a resource
    api_instance.cf_manager_rest_api_put_resource(username, password, resource_id, body=body)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_put_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **resource_id** | **str**| cloudFPGA resource unique identifier | 
 **body** | [**Resource**](Resource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_put_resource_status**
> cf_manager_rest_api_put_resource_status(username, password, resource_id, new_status)

Update status of a resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
resource_id = 'resource_id_example' # str | cloudFPGA resource unique identifier
new_status = 'new_status_example' # str | New status of the resource

try:
    # Update status of a resource
    api_instance.cf_manager_rest_api_put_resource_status(username, password, resource_id, new_status)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_put_resource_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **resource_id** | **str**| cloudFPGA resource unique identifier | 
 **new_status** | **str**| New status of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_put_resources_of_sled_status**
> cf_manager_rest_api_put_resources_of_sled_status(username, password, sled_ip, new_status)

Update status of **all resources** from a specific sled

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
sled_ip = 'sled_ip_example' # str | The ip address of a SM
new_status = 'new_status_example' # str | New status of the resource

try:
    # Update status of **all resources** from a specific sled
    api_instance.cf_manager_rest_api_put_resources_of_sled_status(username, password, sled_ip, new_status)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_put_resources_of_sled_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **sled_ip** | **str**| The ip address of a SM | 
 **new_status** | **str**| New status of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_put_resources_of_sled_status_in_state**
> cf_manager_rest_api_put_resources_of_sled_status_in_state(username, password, sled_ip, status, new_status)

Update status of **all resources** from a specific sled in a specific `{status}`

For example, if this method is called with `PUT /resources/sled/1.2.3.4/AVAILABLE`, then only all `AVAILABLE` resources of Sled `1.2.3.4` are put to to the `new_status`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
sled_ip = 'sled_ip_example' # str | The ip address of a SM
status = 'status_example' # str | Status of the resources that should be updated
new_status = 'new_status_example' # str | New status of the resources

try:
    # Update status of **all resources** from a specific sled in a specific `{status}`
    api_instance.cf_manager_rest_api_put_resources_of_sled_status_in_state(username, password, sled_ip, status, new_status)
except ApiException as e:
    print("Exception when calling ResourcesAdminOnlyApi->cf_manager_rest_api_put_resources_of_sled_status_in_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **sled_ip** | **str**| The ip address of a SM | 
 **status** | **str**| Status of the resources that should be updated | 
 **new_status** | **str**| New status of the resources | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

