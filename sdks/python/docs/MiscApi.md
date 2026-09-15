# jgsp_client.MiscApi

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legacy_api**](MiscApi.md#legacy_api) | **POST** /api/api.php | Generic internal API dispatcher


# **legacy_api**
> object legacy_api(action=action)

Generic internal API dispatcher

Legacy/generic dispatcher. Responds with plain text `ERROR_MISSING_PARAMETERS`
when the `ACTION` parameter is missing. Behaviour with valid actions is unknown —
this endpoint is used by the web front-end.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import jgsp_client
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
    api_instance = jgsp_client.MiscApi(api_client)
    action = 'action_example' # str | Generic action verb. (optional)

    try:
        # Generic internal API dispatcher
        api_response = api_instance.legacy_api(action=action)
        print("The response of MiscApi->legacy_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscApi->legacy_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Generic action verb. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Legacy API payload |  -  |
**400** | Missing ACTION parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

