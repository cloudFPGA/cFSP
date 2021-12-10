# swagger_client.AdministrationAdminOnlyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cf_manager_rest_api_admin_test_instance**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_admin_test_instance) | **PUT** /administration/test_instance/{instance_id} | Test the instance **if not used**
[**cf_manager_rest_api_admin_update_flash**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_admin_update_flash) | **PUT** /administration/update_flash/{resource_id} | Update the flash of a resource **if not used**
[**cf_manager_rest_api_delete_ippool**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_delete_ippool) | **DELETE** /administration/ippool/ | Remove a /24 subnet
[**cf_manager_rest_api_get_all_composable_logic**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_get_all_composable_logic) | **GET** /administration/composablelogic/all/ | Get list of all composable logic
[**cf_manager_rest_api_get_buildscripts_all**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_get_buildscripts_all) | **GET** /administration/buildscripts | Get all registered build script versions
[**cf_manager_rest_api_get_ippool**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_get_ippool) | **GET** /administration/ippool/ | Get all ip addresses in the current pool
[**cf_manager_rest_api_get_mantle_logic_all**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_get_mantle_logic_all) | **GET** /administration/mantle_logic | Get all mantle logics
[**cf_manager_rest_api_get_platform_logic_all**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_get_platform_logic_all) | **GET** /administration/platform_logic | Get all platform logics
[**cf_manager_rest_api_get_single_buildscript**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_get_single_buildscript) | **GET** /administration/buildscripts/{bs_id} | Get details of one registered build script
[**cf_manager_rest_api_get_single_composable_logic**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_get_single_composable_logic) | **GET** /administration/composablelogic/{cl_id}/ | Get details of one composable logic
[**cf_manager_rest_api_post_buildscript**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_post_buildscript) | **POST** /administration/buildscripts | Register a new build script version
[**cf_manager_rest_api_post_ippool**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_post_ippool) | **POST** /administration/ippool/ | Post a new &#x60;/24&#x60; ip pool (subnet)
[**cf_manager_rest_api_post_mantle_logic**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_post_mantle_logic) | **POST** /administration/mantle_logic | Upload a new dynamic platform logic
[**cf_manager_rest_api_post_platform_logic**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_post_platform_logic) | **POST** /administration/platform_logic | Upload a new platform logic
[**cf_manager_rest_api_put_buildscript**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_put_buildscript) | **PUT** /administration/buildscripts/{bs_id} | Update a registered build script
[**cf_manager_rest_api_put_composable_logic_status**](AdministrationAdminOnlyApi.md#cf_manager_rest_api_put_composable_logic_status) | **PUT** /administration/composablelogic/{cl_id}/status/ | Update status of a composable logic

# **cf_manager_rest_api_admin_test_instance**
> InlineResponse2001 cf_manager_rest_api_admin_test_instance(body, username, password, instance_id, dont_verify_memory=dont_verify_memory)

Test the instance **if not used**

This call helps admins to test a specific instance, **if this instance is not used by another user**. This is **intended only for single instances**, not to update one instance out of a cluster.  **If this call fails with `507`** and the FPGA worked without any problems before, then the submitted image probably doesn't work (i.e. `507` doesn't imply a failure of the FPGA board). This will also assign a new ip address to this instance. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
body = swagger_client.TestInstanceInstanceIdBody() # TestInstanceInstanceIdBody | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier
dont_verify_memory = 0 # int | If 1, don't verify the DDR4 memory during setup (optional) (default to 0)

try:
    # Test the instance **if not used**
    api_response = api_instance.cf_manager_rest_api_admin_test_instance(body, username, password, instance_id, dont_verify_memory=dont_verify_memory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_admin_test_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TestInstanceInstanceIdBody**](TestInstanceInstanceIdBody.md)|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 
 **dont_verify_memory** | **int**| If 1, don&#x27;t verify the DDR4 memory during setup | [optional] [default to 0]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_admin_update_flash**
> Resource cf_manager_rest_api_admin_update_flash(username, password, resource_id, pl_id)

Update the flash of a resource **if not used**

This call allows admins to update the flash file of a resource, **if this instance is not used by another user**. If successful, the resource's shell_type is updated and the resource is marked as AVAILABLE. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
resource_id = 'resource_id_example' # str | cloudFPGA resource unique identifier
pl_id = 'pl_id_example' # str | Platform logic unique identifier

try:
    # Update the flash of a resource **if not used**
    api_response = api_instance.cf_manager_rest_api_admin_update_flash(username, password, resource_id, pl_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_admin_update_flash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **resource_id** | **str**| cloudFPGA resource unique identifier | 
 **pl_id** | **str**| Platform logic unique identifier | 

### Return type

[**Resource**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_delete_ippool**
> cf_manager_rest_api_delete_ippool(username, password, subnet_string)

Remove a /24 subnet

Marks the submitted `/24` subnet as `DELETED`. *Note: this will not delete all ip addresses immediately*, `USED` ip addresses remains used until the corresponding `instance` is deleted. For now *only /24 subnets* are supported, so it is enough to submit the subnet base, *e.g. `10.12.200.0`*! 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
subnet_string = 'subnet_string_example' # str | A /24 subnet

try:
    # Remove a /24 subnet
    api_instance.cf_manager_rest_api_delete_ippool(username, password, subnet_string)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_delete_ippool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **subnet_string** | **str**| A /24 subnet | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_all_composable_logic**
> cf_manager_rest_api_get_all_composable_logic(username, password)

Get list of all composable logic

This API call also checks if DEPRECATED or DISCHARGED PLs are still programmed to some resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Get list of all composable logic
    api_instance.cf_manager_rest_api_get_all_composable_logic(username, password)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_get_all_composable_logic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_buildscripts_all**
> list[BuildScript] cf_manager_rest_api_get_buildscripts_all(username, password)

Get all registered build script versions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Get all registered build script versions
    api_response = api_instance.cf_manager_rest_api_get_buildscripts_all(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_get_buildscripts_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

[**list[BuildScript]**](BuildScript.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_ippool**
> list[InlineResponse200] cf_manager_rest_api_get_ippool(username, password)

Get all ip addresses in the current pool

This call returns a list of *all* ip addresses that are currently known, regardless their state. That includes also ip addresses that are marked as `DELETED` but are still in use. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Get all ip addresses in the current pool
    api_response = api_instance.cf_manager_rest_api_get_ippool(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_get_ippool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_mantle_logic_all**
> cf_manager_rest_api_get_mantle_logic_all(username, password)

Get all mantle logics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Get all mantle logics
    api_instance.cf_manager_rest_api_get_mantle_logic_all(username, password)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_get_mantle_logic_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_platform_logic_all**
> cf_manager_rest_api_get_platform_logic_all(username, password)

Get all platform logics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Get all platform logics
    api_instance.cf_manager_rest_api_get_platform_logic_all(username, password)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_get_platform_logic_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_single_buildscript**
> BuildScript cf_manager_rest_api_get_single_buildscript(username, password, bs_id)

Get details of one registered build script

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
bs_id = 56 # int | ID of a registered build script

try:
    # Get details of one registered build script
    api_response = api_instance.cf_manager_rest_api_get_single_buildscript(username, password, bs_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_get_single_buildscript: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **bs_id** | **int**| ID of a registered build script | 

### Return type

[**BuildScript**](BuildScript.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_single_composable_logic**
> cf_manager_rest_api_get_single_composable_logic(username, password, cl_id)

Get details of one composable logic

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cl_id = 56 # int | ID of a composable logic (Static Shell or Mantles)

try:
    # Get details of one composable logic
    api_instance.cf_manager_rest_api_get_single_composable_logic(username, password, cl_id)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_get_single_composable_logic: %s\n" % e)
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

# **cf_manager_rest_api_post_buildscript**
> BuildScript cf_manager_rest_api_post_buildscript(username, password, body=body)

Register a new build script version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
body = swagger_client.BuildScript() # BuildScript |  (optional)

try:
    # Register a new build script version
    api_response = api_instance.cf_manager_rest_api_post_buildscript(username, password, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_post_buildscript: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **body** | [**BuildScript**](BuildScript.md)|  | [optional] 

### Return type

[**BuildScript**](BuildScript.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_ippool**
> cf_manager_rest_api_post_ippool(username, password, subnet_string, gateway_string, mask_string)

Post a new `/24` ip pool (subnet)

Introduces a new `/24` ip pool that is available for assignment to FPGAs.  For now, **only /24 subnets as ip pool** are supported, so it is enough to submit the subnet base, *e.g. `10.12.200.0`*!  The submitted *gateway*, e.g. `10.12.0.1`, will be used as gateway address for all FPGAs that get an ip address out of this subnet assigned. Multiple ip pools can have the same gateway. Subnetmasks, e.g. `255.255.0.0` are used in a similar way.  Hence, the subnetmask **can not** be derived from the subnet itself. Maybe it is possible that the FPGAs of a new subnet can also talk to other subnets, so the subnet mask must be submitted separately. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
subnet_string = 'subnet_string_example' # str | A /24 subnet
gateway_string = 'gateway_string_example' # str | The gateway for this subnet
mask_string = 'mask_string_example' # str | The subnetmask for this subnet

try:
    # Post a new `/24` ip pool (subnet)
    api_instance.cf_manager_rest_api_post_ippool(username, password, subnet_string, gateway_string, mask_string)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_post_ippool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **subnet_string** | **str**| A /24 subnet | 
 **gateway_string** | **str**| The gateway for this subnet | 
 **mask_string** | **str**| The subnetmask for this subnet | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_mantle_logic**
> cf_manager_rest_api_post_mantle_logic(image_details, bin_file, sig_file, pr_verify_rpt, username, password)

Upload a new dynamic platform logic

This uploads an new Image for the DYNAMIC PLATFORM LOGIC (aka FPGA PR binfile). It **must** contain the corresponding .sig file that was produced by the build. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
image_details = 'image_details_example' # str | 
bin_file = 'bin_file_example' # str | 
sig_file = 'sig_file_example' # str | 
pr_verify_rpt = 'pr_verify_rpt_example' # str | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Upload a new dynamic platform logic
    api_instance.cf_manager_rest_api_post_mantle_logic(image_details, bin_file, sig_file, pr_verify_rpt, username, password)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_post_mantle_logic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_details** | **str**|  | 
 **bin_file** | **str**|  | 
 **sig_file** | **str**|  | 
 **pr_verify_rpt** | **str**|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_platform_logic**
> cf_manager_rest_api_post_platform_logic(image_details, dcp_file, bit_file, mcs_file, sig_file, pr_verify_rpt, username, password)

Upload a new platform logic

This uploads an new Image for the STATIC PLATFORM LOGIC (aka FPGA bitfile and flash mcsfile) and the corresponding dcp, for app / mantle builds. It also **must** contain the corresponding admin.sig file that was produced by the build. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
image_details = 'image_details_example' # str | 
dcp_file = 'dcp_file_example' # str | 
bit_file = 'bit_file_example' # str | 
mcs_file = 'mcs_file_example' # str | 
sig_file = 'sig_file_example' # str | 
pr_verify_rpt = 'pr_verify_rpt_example' # str | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Upload a new platform logic
    api_instance.cf_manager_rest_api_post_platform_logic(image_details, dcp_file, bit_file, mcs_file, sig_file, pr_verify_rpt, username, password)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_post_platform_logic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_details** | **str**|  | 
 **dcp_file** | **str**|  | 
 **bit_file** | **str**|  | 
 **mcs_file** | **str**|  | 
 **sig_file** | **str**|  | 
 **pr_verify_rpt** | **str**|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_put_buildscript**
> cf_manager_rest_api_put_buildscript(username, password, bs_id, body=body)

Update a registered build script

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
bs_id = 56 # int | ID of a registered build script
body = swagger_client.BuildScript() # BuildScript |  (optional)

try:
    # Update a registered build script
    api_instance.cf_manager_rest_api_put_buildscript(username, password, bs_id, body=body)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_put_buildscript: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **bs_id** | **int**| ID of a registered build script | 
 **body** | [**BuildScript**](BuildScript.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_put_composable_logic_status**
> cf_manager_rest_api_put_composable_logic_status(username, password, cl_id, new_status)

Update status of a composable logic

This call changes the status of a composable logic, to reflect the CL lifecycle (see doc).  If the status is changed to DEPRECATED or DISCHARGED, all resources are checked if some still use this CL. If yes, a warning is issued and the list of affected resources returned (response 202).  Currently, *only* the status can be changed, since all the other properties of a CL are considered static and if they should be changed, it is better to upload a new CL. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrationAdminOnlyApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cl_id = 56 # int | ID of a composable logic (Static Shell or Mantles)
new_status = 'new_status_example' # str | New status of the composable logic

try:
    # Update status of a composable logic
    api_instance.cf_manager_rest_api_put_composable_logic_status(username, password, cl_id, new_status)
except ApiException as e:
    print("Exception when calling AdministrationAdminOnlyApi->cf_manager_rest_api_put_composable_logic_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cl_id** | **int**| ID of a composable logic (Static Shell or Mantles) | 
 **new_status** | **str**| New status of the composable logic | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

