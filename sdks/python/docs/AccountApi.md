# jgsp_client.AccountApi

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_action**](AccountApi.md#account_action) | **POST** /publicapi/v1/rest_options/android_login.php | Account actions (login, register, reset password…)


# **account_action**
> AccountAction200Response account_action(action, email=email, password=password, first_name=first_name, last_name=last_name)

Account actions (login, register, reset password…)

Single dispatcher endpoint for account-related actions, selected via the `action`
form parameter. Observed behaviours (September 2026):

* `action=register` → `{"success":false,"msg":"SIGNUP_FORM_NOT_CONFIGURED"}` (registration disabled for this operator)
* `action=login` and most other verbs → `[]` (empty array)
* missing `action` → plain text `POTREBAN JE PARAMETAR ACTION` ("ACTION parameter is required")

The full set of actions is not publicly documented; the NSmart APK shows
login, register, social login (Google/Facebook), reset password and email
verification flows.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import jgsp_client
from jgsp_client.models.account_action200_response import AccountAction200Response
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
    api_instance = jgsp_client.AccountApi(api_client)
    action = 'action_example' # str | Account action verb.
    email = 'email_example' # str | Used by login/register/reset flows. (optional)
    password = 'password_example' # str |  (optional)
    first_name = 'first_name_example' # str |  (optional)
    last_name = 'last_name_example' # str |  (optional)

    try:
        # Account actions (login, register, reset password…)
        api_response = api_instance.account_action(action, email=email, password=password, first_name=first_name, last_name=last_name)
        print("The response of AccountApi->account_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Account action verb. | 
 **email** | **str**| Used by login/register/reset flows. | [optional] 
 **password** | **str**|  | [optional] 
 **first_name** | **str**|  | [optional] 
 **last_name** | **str**|  | [optional] 

### Return type

[**AccountAction200Response**](AccountAction200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action-dependent result (array or status object) |  -  |
**400** | Missing action parameter (plain text, not JSON) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

