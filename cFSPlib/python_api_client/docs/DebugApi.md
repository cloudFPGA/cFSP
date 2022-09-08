# swagger_client.DebugApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cf_manager_rest_api_delete_debug_connection**](DebugApi.md#cf_manager_rest_api_delete_debug_connection) | **DELETE** /debug/ila_connection/{instance_id} | Deletes an existing connection to the &#x60;hw_server&#x60; of this instance
[**cf_manager_rest_api_get_all_debug_connections**](DebugApi.md#cf_manager_rest_api_get_all_debug_connections) | **GET** /debug/open_ila_connections | Requests a list of running &#x60;hw_server&#x60;s on all instances (admin only)
[**cf_manager_rest_api_get_all_debug_connections_of_user**](DebugApi.md#cf_manager_rest_api_get_all_debug_connections_of_user) | **GET** /debug/ila_connections | Returns all open &#x60;hw_server&#x60; of a user
[**cf_manager_rest_api_get_debug_connection**](DebugApi.md#cf_manager_rest_api_get_debug_connection) | **GET** /debug/ila_connection/{instance_id} | Requests a connection to the &#x60;hw_server&#x60; of this instance
[**cf_manager_rest_api_get_flight_recorder_cluster**](DebugApi.md#cf_manager_rest_api_get_flight_recorder_cluster) | **GET** /clusters/{cluster_id}/flight_recorder_data | Requests network runtime information of all instances
[**cf_manager_rest_api_get_flight_recorder_instance**](DebugApi.md#cf_manager_rest_api_get_flight_recorder_instance) | **GET** /instances/{instance_id}/flight_recorder_data | Requests network runtime information

# **cf_manager_rest_api_delete_debug_connection**
> cf_manager_rest_api_delete_debug_connection(username, password, instance_id)

Deletes an existing connection to the `hw_server` of this instance

This deletes the *connection to the* `hw_server`. This **does not imply** that the `hw_server` itself is stopped too. The `hw_server` is only stopped if there is no other open debug connection to the connected JTAG probe (some probes are connected to a JTAG chain). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier

try:
    # Deletes an existing connection to the `hw_server` of this instance
    api_instance.cf_manager_rest_api_delete_debug_connection(username, password, instance_id)
except ApiException as e:
    print("Exception when calling DebugApi->cf_manager_rest_api_delete_debug_connection: %s\n" % e)
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

# **cf_manager_rest_api_get_all_debug_connections**
> list[InlineResponse2004] cf_manager_rest_api_get_all_debug_connections(username, password)

Requests a list of running `hw_server`s on all instances (admin only)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Requests a list of running `hw_server`s on all instances (admin only)
    api_response = api_instance.cf_manager_rest_api_get_all_debug_connections(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->cf_manager_rest_api_get_all_debug_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_all_debug_connections_of_user**
> list[InlineResponse2004] cf_manager_rest_api_get_all_debug_connections_of_user(username, password)

Returns all open `hw_server` of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password

try:
    # Returns all open `hw_server` of a user
    api_response = api_instance.cf_manager_rest_api_get_all_debug_connections_of_user(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->cf_manager_rest_api_get_all_debug_connections_of_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_debug_connection**
> InlineResponse2003 cf_manager_rest_api_get_debug_connection(username, password, instance_id, ip_address=ip_address)

Requests a connection to the `hw_server` of this instance

This returns an IP-address and a TCP port to enter into the *remote debugging dialog* in `vivado_lab`. **Only the IP-address that issues this request will be allowed to connect (or the specified IP address).**  If there is already an open debug connection to the specified instance, the existing data will be returned. That means, to debug the same instance on a different client, the connection must be deleted first.  Due to ongoing Hardware Development it is possible that there are more than one FPGA visible in the debug connection (some FPGAs share a JTAG probe via a JTAG chain). **You are only allowed to interact with the device that is stated in the `device` value in the response from the server.** (The Resource Manager assures that the devices in a JTAG chain are only given to members of the same project, so if you interact with other devices, you will disturb your direct colleges). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier
ip_address = '0.0.0.0' # str | IPv4 address of the Debuging client if different from requesting client (only this addres will be allowed to connect). (optional) (default to 0.0.0.0)

try:
    # Requests a connection to the `hw_server` of this instance
    api_response = api_instance.cf_manager_rest_api_get_debug_connection(username, password, instance_id, ip_address=ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->cf_manager_rest_api_get_debug_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 
 **ip_address** | **str**| IPv4 address of the Debuging client if different from requesting client (only this addres will be allowed to connect). | [optional] [default to 0.0.0.0]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_flight_recorder_cluster**
> InlineResponse2002 cf_manager_rest_api_get_flight_recorder_cluster(username, password, cluster_id)

Requests network runtime information of all instances

Requests and returns the status information of the Network Routing Core of all instances in this cluster. The call returns two lists, that contain both the same content, just differently sorted (one ascending by instance id, one ascending by rank id).  `Attention:` There may be a delay of a few seconds until the counters are updated after the packets were processed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
cluster_id = 56 # int | ID of a cluster

try:
    # Requests network runtime information of all instances
    api_response = api_instance.cf_manager_rest_api_get_flight_recorder_cluster(username, password, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->cf_manager_rest_api_get_flight_recorder_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **cluster_id** | **int**| ID of a cluster | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cf_manager_rest_api_get_flight_recorder_instance**
> list[list[str]] cf_manager_rest_api_get_flight_recorder_instance(username, password, instance_id)

Requests network runtime information

Requests and returns the status information of the Network Routing Core of this FPGA instance. `Attention:` There may be a delay of a few seconds until the counters are updated after the packets were processed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DebugApi()
username = 'username_example' # str | OpenStack username
password = 'password_example' # str | OpenStack password
instance_id = 'instance_id_example' # str | ROLE instance unique identifier

try:
    # Requests network runtime information
    api_response = api_instance.cf_manager_rest_api_get_flight_recorder_instance(username, password, instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->cf_manager_rest_api_get_flight_recorder_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| OpenStack username | 
 **password** | **str**| OpenStack password | 
 **instance_id** | **str**| ROLE instance unique identifier | 

### Return type

**list[list[str]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

