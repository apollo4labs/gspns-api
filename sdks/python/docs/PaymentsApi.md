# jgsp_client.PaymentsApi

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allsecure_payment**](PaymentsApi.md#allsecure_payment) | **POST** /publicapi/v1/rest_options/android_allsecure.php | AllSecure payment operations


# **allsecure_payment**
> object allsecure_payment(action)

AllSecure payment operations

Payment gateway (AllSecure / Credorax) integration used for card payments,
tokenization and validation. Class names in the APK: `AllSecureValidationApi`,
`AllSecureFinalizeApi`, `AllSecureCheckStatusApi`.


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
    api_instance = jgsp_client.PaymentsApi(api_client)
    action = 'action_example' # str | e.g. validate, finalize, check_status

    try:
        # AllSecure payment operations
        api_response = api_instance.allsecure_payment(action)
        print("The response of PaymentsApi->allsecure_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->allsecure_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| e.g. validate, finalize, check_status | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment status payload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

