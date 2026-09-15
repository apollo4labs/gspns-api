# WalletCardsApi

All URIs are relative to *https://online.nsmart.rs*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addOrConnectCard**](WalletCardsApi.md#addorconnectcard) | **POST** /publicapi/v1/rest_options/android_add_or_connect_card.php | Add or connect a transport card |
| [**additionalOptions**](WalletCardsApi.md#additionaloptions) | **POST** /publicapi/v1/rest_options/android_additional_options.php | Additional card/ticket options |
| [**additionalSettings**](WalletCardsApi.md#additionalsettings) | **POST** /publicapi/v1/rest_options/android_additional_settings.php | Additional settings |
| [**prepaidCardsLog**](WalletCardsApi.md#prepaidcardslog) | **POST** /publicapi/v1/rest_options/android_prepaid_cards_log_online.php | Prepaid card online log |



## addOrConnectCard

> ApiStatus addOrConnectCard(action, cardUid)

Add or connect a transport card

Attaches a physical NFC card or prepaid card to the user\&#39;s account.

### Example

```ts
import {
  Configuration,
  WalletCardsApi,
} from '';
import type { AddOrConnectCardRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new WalletCardsApi(config);

  const body = {
    // string
    action: action_example,
    // string | UID of the physical card being connected. (optional)
    cardUid: cardUid_example,
  } satisfies AddOrConnectCardRequest;

  try {
    const data = await api.addOrConnectCard(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **action** | `string` |  | [Defaults to `undefined`] |
| **cardUid** | `string` | UID of the physical card being connected. | [Optional] [Defaults to `undefined`] |

### Return type

[**ApiStatus**](ApiStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of the card operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## additionalOptions

> Array&lt;any&gt; additionalOptions(action)

Additional card/ticket options

Dispatcher for extra options (prepaid cards, additional settings). Observed to return &#x60;[]&#x60; for unknown &#x60;action&#x60; values. Real action verbs are embedded in the NSmart APK (card types, existing NFC/paper cards, online QR codes…). 

### Example

```ts
import {
  Configuration,
  WalletCardsApi,
} from '';
import type { AdditionalOptionsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new WalletCardsApi(config);

  const body = {
    // string | Option action verb.
    action: action_example,
  } satisfies AdditionalOptionsRequest;

  try {
    const data = await api.additionalOptions(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **action** | `string` | Option action verb. | [Defaults to `undefined`] |

### Return type

**Array<any>**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Options payload (array of objects) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## additionalSettings

> Array&lt;any&gt; additionalSettings(action)

Additional settings

Dispatcher for additional user/operator settings. Returns &#x60;[]&#x60; for unknown actions.

### Example

```ts
import {
  Configuration,
  WalletCardsApi,
} from '';
import type { AdditionalSettingsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new WalletCardsApi(config);

  const body = {
    // string
    action: action_example,
  } satisfies AdditionalSettingsRequest;

  try {
    const data = await api.additionalSettings(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **action** | `string` |  | [Defaults to `undefined`] |

### Return type

**Array<any>**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings payload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## prepaidCardsLog

> Array&lt;any&gt; prepaidCardsLog(action)

Prepaid card online log

Uploads or fetches the online log of prepaid card usage.

### Example

```ts
import {
  Configuration,
  WalletCardsApi,
} from '';
import type { PrepaidCardsLogRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new WalletCardsApi(config);

  const body = {
    // string
    action: action_example,
  } satisfies PrepaidCardsLogRequest;

  try {
    const data = await api.prepaidCardsLog(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **action** | `string` |  | [Defaults to `undefined`] |

### Return type

**Array<any>**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prepaid card log entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

