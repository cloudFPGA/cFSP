# swagger_client.ProjectsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cf_manager_rest_api_get_project_quota**](ProjectsApi.md#cf_manager_rest_api_get_project_quota) | **GET** /projects/{project_name}/quota/ | Get the current quota of a project
[**cf_manager_rest_api_list_projects**](ProjectsApi.md#cf_manager_rest_api_list_projects) | **GET** /projects/ | List the projects the user belongs to
[**cf_manager_rest_api_post_project_quota**](ProjectsApi.md#cf_manager_rest_api_post_project_quota) | **POST** /projects/{project_name}/quota/ | Post a new (or update existent) quota of a project (admin only)

# **cf_manager_rest_api_get_project_quota**
> Quota cf_manager_rest_api_get_project_quota(username, password, project_name)

Get the current quota of a project

With this call a user can check how many FPGAs of his project are available for usage. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
project_name = 'project_name_example' # str | Name of a OpenStack project

try:
    # Get the current quota of a project
    api_response = api_instance.cf_manager_rest_api_get_project_quota(username, password, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cf_manager_rest_api_get_project_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **project_name** | **str**| Name of a OpenStack project | 

### Return type

[**Quota**](Quota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_list_projects**
> list[str] cf_manager_rest_api_list_projects(username, password)

List the projects the user belongs to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # List the projects the user belongs to
    api_response = api_instance.cf_manager_rest_api_list_projects(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->cf_manager_rest_api_list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_project_quota**
> cf_manager_rest_api_post_project_quota(username, password, project_name, body=body)

Post a new (or update existent) quota of a project (admin only)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
project_name = 'project_name_example' # str | Name of a OpenStack project
body = swagger_client.Quota() # Quota |  (optional)

try:
    # Post a new (or update existent) quota of a project (admin only)
    api_instance.cf_manager_rest_api_post_project_quota(username, password, project_name, body=body)
except ApiException as e:
    print("Exception when calling ProjectsApi->cf_manager_rest_api_post_project_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **project_name** | **str**| Name of a OpenStack project | 
 **body** | [**Quota**](Quota.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

