# swagger_client.ImagesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cf_manager_rest_api_delete_image**](ImagesApi.md#cf_manager_rest_api_delete_image) | **DELETE** /images/{image_id} | Delete an image
[**cf_manager_rest_api_get_image_single**](ImagesApi.md#cf_manager_rest_api_get_image_single) | **GET** /images/{image_id} | Get an image
[**cf_manager_rest_api_get_images**](ImagesApi.md#cf_manager_rest_api_get_images) | **GET** /images | Get all images of a user
[**cf_manager_rest_api_post_app_logic**](ImagesApi.md#cf_manager_rest_api_post_app_logic) | **POST** /images/app_logic | Upload an image of type &#x60;app logic&#x60;
[**cf_manager_rest_api_post_images**](ImagesApi.md#cf_manager_rest_api_post_images) | **POST** /images | Upload an image

# **cf_manager_rest_api_delete_image**
> cf_manager_rest_api_delete_image(username, password, image_id)

Delete an image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
image_id = 'image_id_example' # str | Image unique identifier

try:
    # Delete an image
    api_instance.cf_manager_rest_api_delete_image(username, password, image_id)
except ApiException as e:
    print("Exception when calling ImagesApi->cf_manager_rest_api_delete_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **image_id** | **str**| Image unique identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_image_single**
> Image cf_manager_rest_api_get_image_single(username, password, image_id)

Get an image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
image_id = 'image_id_example' # str | Image unique identifier

try:
    # Get an image
    api_response = api_instance.cf_manager_rest_api_get_image_single(username, password, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->cf_manager_rest_api_get_image_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **image_id** | **str**| Image unique identifier | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_images**
> list[Image] cf_manager_rest_api_get_images(username, password, limit=limit)

Get all images of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all images of a user
    api_response = api_instance.cf_manager_rest_api_get_images(username, password, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->cf_manager_rest_api_get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**list[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_app_logic**
> Image cf_manager_rest_api_post_app_logic(image_details, image_file, sig_file, pr_verify_rpt, username, password)

Upload an image of type `app logic`

This uploads an new image (aka FPGA **bin**file). **This method is for the app logic in case of partial reconfiguration building on platform logics**. The `id` of the uploaded Image can then be used to create *Instances* or *Clusters*. It **must** contain the corresponding .sig file that was produced by the build. The resulting image can be viewed and deleted like other images. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_details = 'image_details_example' # str | 
image_file = 'image_file_example' # str | 
sig_file = 'sig_file_example' # str | 
pr_verify_rpt = 'pr_verify_rpt_example' # str | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Upload an image of type `app logic`
    api_response = api_instance.cf_manager_rest_api_post_app_logic(image_details, image_file, sig_file, pr_verify_rpt, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->cf_manager_rest_api_post_app_logic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_details** | **str**|  | 
 **image_file** | **str**|  | 
 **sig_file** | **str**|  | 
 **pr_verify_rpt** | **str**|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_post_images**
> Image cf_manager_rest_api_post_images(image_details, image_file, pr_verify_rpt, username, password)

Upload an image

This uploads an new Image (aka FPGA bitfile). The `id` of the uploaded Image can then be used to create *Instances* or *Clusters*.  If the bitfile **is not a partial bitfile**, the *image_detail* **property `breed` must be `\"SHELL\"`**. The *image_detail* property `shell_type` is only relevant for the partial reconfiguration flow, but cannot be empty (e.g. enter `\"NO_PR\"`). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image_details = 'image_details_example' # str | 
image_file = 'image_file_example' # str | 
pr_verify_rpt = 'pr_verify_rpt_example' # str | 
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Upload an image
    api_response = api_instance.cf_manager_rest_api_post_images(image_details, image_file, pr_verify_rpt, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->cf_manager_rest_api_post_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_details** | **str**|  | 
 **image_file** | **str**|  | 
 **pr_verify_rpt** | **str**|  | 
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

