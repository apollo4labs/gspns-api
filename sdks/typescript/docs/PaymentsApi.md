# PaymentsApi

All URIs are relative to *https://online.nsmart.rs*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allsecurePayment**](PaymentsApi.md#allsecurepayment) | **POST** /publicapi/v1/rest_options/android_allsecure.php | AllSecure payment operations |



## allsecurePayment

> object allsecurePayment(action)

AllSecure payment operations

Payment gateway (AllSecure / Credorax) integration used for card payments, tokenization and validation. Class names in the APK: &#x60;AllSecureValidationApi&#x60;, &#x60;AllSecureFinalizeApi&#x60;, &#x60;AllSecureCheckStatusApi&#x60;. 

### Example

```ts
import {
  Configuration,
  PaymentsApi,
} from '';
import type { AllsecurePaymentRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new PaymentsApi(config);

  const body = {
    // string | e.g. validate, finalize, check_status
    action: action_example,
  } satisfies AllsecurePaymentRequest;

  try {
    const data = await api.allsecurePayment(body);
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
| **action** | `string` | e.g. validate, finalize, check_status | [Defaults to `undefined`] |

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payment status payload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

