# jgsp_client.WalletCardsApi

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_connect_card**](WalletCardsApi.md#add_or_connect_card) | **POST** /publicapi/v1/rest_options/android_add_or_connect_card.php | Add or connect a transport card
[**additional_options**](WalletCardsApi.md#additional_options) | **POST** /publicapi/v1/rest_options/android_additional_options.php | Additional card/ticket options
[**additional_settings**](WalletCardsApi.md#additional_settings) | **POST** /publicapi/v1/rest_options/android_additional_settings.php | Additional settings
[**prepaid_cards_log**](WalletCardsApi.md#prepaid_cards_log) | **POST** /publicapi/v1/rest_options/android_prepaid_cards_log_online.php | Prepaid card online log


# **add_or_connect_card**
> ApiStatus add_or_connect_card(action, card_uid=card_uid)

Add or connect a transport card

Attaches a physical NFC card or prepaid card to the user's account.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import jgsp_client
from jgsp_client.models.api_status import ApiStatus
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
    api_instance = jgsp_client.WalletCardsApi(api_client)
    action = 'action_example' # str | 
    card_uid = 'card_uid_example' # str | UID of the physical card being connected. (optional)

    try:
        # Add or connect a transport card
        api_response = api_instance.add_or_connect_card(action, card_uid=card_uid)
        print("The response of WalletCardsApi->add_or_connect_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletCardsApi->add_or_connect_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | 
 **card_uid** | **str**| UID of the physical card being connected. | [optional] 

### Return type

[**ApiStatus**](ApiStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of the card operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **additional_options**
> List[object] additional_options(action)

Additional card/ticket options

Dispatcher for extra options (prepaid cards, additional settings). Observed to
return `[]` for unknown `action` values. Real action verbs are embedded in the
NSmart APK (card types, existing NFC/paper cards, online QR codes…).


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
    api_instance = jgsp_client.WalletCardsApi(api_client)
    action = 'action_example' # str | Option action verb.

    try:
        # Additional card/ticket options
        api_response = api_instance.additional_options(action)
        print("The response of WalletCardsApi->additional_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletCardsApi->additional_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Option action verb. | 

### Return type

**List[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Options payload (array of objects) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **additional_settings**
> List[object] additional_settings(action)

Additional settings

Dispatcher for additional user/operator settings. Returns `[]` for unknown actions.

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
    api_instance = jgsp_client.WalletCardsApi(api_client)
    action = 'action_example' # str | 

    try:
        # Additional settings
        api_response = api_instance.additional_settings(action)
        print("The response of WalletCardsApi->additional_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletCardsApi->additional_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | 

### Return type

**List[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings payload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepaid_cards_log**
> List[object] prepaid_cards_log(action)

Prepaid card online log

Uploads or fetches the online log of prepaid card usage.

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
    api_instance = jgsp_client.WalletCardsApi(api_client)
    action = 'action_example' # str | 

    try:
        # Prepaid card online log
        api_response = api_instance.prepaid_cards_log(action)
        print("The response of WalletCardsApi->prepaid_cards_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletCardsApi->prepaid_cards_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | 

### Return type

**List[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prepaid card log entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

