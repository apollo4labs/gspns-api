# jgsp_client.NetworkApi

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network**](NetworkApi.md#get_network) | **POST** /publicapi/v1/networkextended.php | Get the full transport network (cities with stations)
[**get_network_get**](NetworkApi.md#get_network_get) | **GET** /publicapi/v1/networkextended.php | Get the transport network (GET variant)


# **get_network**
> Network get_network(get_network_request)

Get the full transport network (cities with stations)

Returns every city served by the network, each with its station IDs, "pairs" (line
pair IDs per station), default station, coordinates and country.

**Novi Sad** is city `id: 72` with `452` stations (default station `7`).

⚠️ The response body is ~1.2 MB and the server can corrupt/truncate it mid-stream —
re-request on parse failure (see info section).


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import jgsp_client
from jgsp_client.models.get_network_request import GetNetworkRequest
from jgsp_client.models.network import Network
from jgsp_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://online.nsmart.rs
# See configuration.py for a list of all supported configuration parameters.
configuration = jgsp_client.Configuration(
    host = "https://online.nsmart.rs"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with jgsp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jgsp_client.NetworkApi(api_client)
    get_network_request = {"action":"get_cities_extended"} # GetNetworkRequest | 

    try:
        # Get the full transport network (cities with stations)
        api_response = api_instance.get_network(get_network_request)
        print("The response of NetworkApi->get_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->get_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_network_request** | [**GetNetworkRequest**](GetNetworkRequest.md)|  | 

### Return type

[**Network**](Network.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The complete network (cities → stations → pairs) |  -  |
**403** | Missing/invalid API key or unauthenticated request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_get**
> Network get_network_get(action)

Get the transport network (GET variant)

Same as POST but with the action passed as a query parameter.
**Note:** as of September 2026 the server returned `403 Forbidden` for unauthenticated
GET requests without the API key; with the key it works. Kept for completeness.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import jgsp_client
from jgsp_client.models.network import Network
from jgsp_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://online.nsmart.rs
# See configuration.py for a list of all supported configuration parameters.
configuration = jgsp_client.Configuration(
    host = "https://online.nsmart.rs"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with jgsp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jgsp_client.NetworkApi(api_client)
    action = 'get_cities_extended' # str |  (default to 'get_cities_extended')

    try:
        # Get the transport network (GET variant)
        api_response = api_instance.get_network_get(action)
        print("The response of NetworkApi->get_network_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->get_network_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | [default to &#39;get_cities_extended&#39;]

### Return type

[**Network**](Network.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The complete network payload |  -  |
**403** | Missing/invalid API key or unauthenticated request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

