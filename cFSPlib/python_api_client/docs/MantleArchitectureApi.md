# swagger_client.MantleArchitectureApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cf_manager_rest_api_get_composable_logic_all_part**](MantleArchitectureApi.md#cf_manager_rest_api_get_composable_logic_all_part) | **GET** /composablelogic/by_part/{part} | Returns all composable logics of the given part that are &#x60;IN_USE&#x60;
[**cf_manager_rest_api_get_composable_logic_all_prp**](MantleArchitectureApi.md#cf_manager_rest_api_get_composable_logic_all_prp) | **GET** /composablelogic/by_prp/{prp} | Returns all composable logics of the given prp-type that are &#x60;IN_USE&#x60;
[**cf_manager_rest_api_get_composable_logic_all_shell_type**](MantleArchitectureApi.md#cf_manager_rest_api_get_composable_logic_all_shell_type) | **GET** /composablelogic/by_shell/{shell_type} | Returns all composable logics of the given shell-type that are &#x60;IN_USE&#x60;
[**cf_manager_rest_api_get_composable_logic_dcp**](MantleArchitectureApi.md#cf_manager_rest_api_get_composable_logic_dcp) | **GET** /composablelogic/{cl_id}/dcp | Get the dcp file of a composable logic
[**cf_manager_rest_api_get_composable_logic_meta**](MantleArchitectureApi.md#cf_manager_rest_api_get_composable_logic_meta) | **GET** /composablelogic/{cl_id}/meta | Get the meta data of a composable logic

# **cf_manager_rest_api_get_composable_logic_all_part**
> cf_manager_rest_api_get_composable_logic_all_part(username, password, part)

Returns all composable logics of the given part that are `IN_USE`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MantleArchitectureApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
part = 'part_example' # str | The part of the composable logics

try:
    # Returns all composable logics of the given part that are `IN_USE`
    api_instance.cf_manager_rest_api_get_composable_logic_all_part(username, password, part)
except ApiException as e:
    print("Exception when calling MantleArchitectureApi->cf_manager_rest_api_get_composable_logic_all_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **part** | **str**| The part of the composable logics | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_composable_logic_all_prp**
> cf_manager_rest_api_get_composable_logic_all_prp(username, password, prp)

Returns all composable logics of the given prp-type that are `IN_USE`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MantleArchitectureApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
prp = 56 # int | The prp-level of the composable logics

try:
    # Returns all composable logics of the given prp-type that are `IN_USE`
    api_instance.cf_manager_rest_api_get_composable_logic_all_prp(username, password, prp)
except ApiException as e:
    print("Exception when calling MantleArchitectureApi->cf_manager_rest_api_get_composable_logic_all_prp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **prp** | **int**| The prp-level of the composable logics | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_composable_logic_all_shell_type**
> cf_manager_rest_api_get_composable_logic_all_shell_type(username, password, shell_type)

Returns all composable logics of the given shell-type that are `IN_USE`

If the resulting list is empty, the shell_type is invalid (or no such composalbe logics exist).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MantleArchitectureApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
shell_type = 'shell_type_example' # str | Name of cloudFPGA Shell

try:
    # Returns all composable logics of the given shell-type that are `IN_USE`
    api_instance.cf_manager_rest_api_get_composable_logic_all_shell_type(username, password, shell_type)
except ApiException as e:
    print("Exception when calling MantleArchitectureApi->cf_manager_rest_api_get_composable_logic_all_shell_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **shell_type** | **str**| Name of cloudFPGA Shell | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_composable_logic_dcp**
> cf_manager_rest_api_get_composable_logic_dcp(username, password, cl_id)

Get the dcp file of a composable logic

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MantleArchitectureApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cl_id = 56 # int | ID of a composable logic (Static Shell or Mantles)

try:
    # Get the dcp file of a composable logic
    api_instance.cf_manager_rest_api_get_composable_logic_dcp(username, password, cl_id)
except ApiException as e:
    print("Exception when calling MantleArchitectureApi->cf_manager_rest_api_get_composable_logic_dcp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cl_id** | **int**| ID of a composable logic (Static Shell or Mantles) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_composable_logic_meta**
> Image cf_manager_rest_api_get_composable_logic_meta(username, password, cl_id)

Get the meta data of a composable logic

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MantleArchitectureApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cl_id = 56 # int | ID of a composable logic (Static Shell or Mantles)

try:
    # Get the meta data of a composable logic
    api_response = api_instance.cf_manager_rest_api_get_composable_logic_meta(username, password, cl_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MantleArchitectureApi->cf_manager_rest_api_get_composable_logic_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cl_id** | **int**| ID of a composable logic (Static Shell or Mantles) | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

