# MiscApi

All URIs are relative to *https://online.nsmart.rs*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**legacyApi**](MiscApi.md#legacyapi) | **POST** /api/api.php | Generic internal API dispatcher |



## legacyApi

> object legacyApi(aCTION)

Generic internal API dispatcher

Legacy/generic dispatcher. Responds with plain text &#x60;ERROR_MISSING_PARAMETERS&#x60; when the &#x60;ACTION&#x60; parameter is missing. Behaviour with valid actions is unknown — this endpoint is used by the web front-end. 

### Example

```ts
import {
  Configuration,
  MiscApi,
} from '';
import type { LegacyApiRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new MiscApi(config);

  const body = {
    // string | Generic action verb. (optional)
    aCTION: aCTION_example,
  } satisfies LegacyApiRequest;

  try {
    const data = await api.legacyApi(body);
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
| **aCTION** | `string` | Generic action verb. | [Optional] [Defaults to `undefined`] |

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`, `text/plain`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Legacy API payload |  -  |
| **400** | Missing ACTION parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

