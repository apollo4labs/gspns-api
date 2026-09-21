# NetworkApi

All URIs are relative to *https://online.nsmart.rs*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetwork**](NetworkApi.md#getnetworkoperation) | **POST** /publicapi/v1/networkextended.php | Get the full transport network (cities with stations) |
| [**getNetworkGet**](NetworkApi.md#getnetworkget) | **GET** /publicapi/v1/networkextended.php | Get the transport network (GET variant) |



## getNetwork

> Network getNetwork(getNetworkRequest)

Get the full transport network (cities with stations)

Returns every city served by the network, each with its station IDs, \&quot;pairs\&quot; (line pair IDs per station), default station, coordinates and country.  **Novi Sad** is city &#x60;id: 72&#x60; with &#x60;452&#x60; stations (default station &#x60;7&#x60;).  ⚠️ The response body is ~1.2 MB and the server can corrupt/truncate it mid-stream — re-request on parse failure (see info section). 

### Example

```ts
import {
  Configuration,
  NetworkApi,
} from '';
import type { GetNetworkOperationRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new NetworkApi(config);

  const body = {
    // GetNetworkRequest
    getNetworkRequest: {"action":"get_cities_extended"},
  } satisfies GetNetworkOperationRequest;

  try {
    const data = await api.getNetwork(body);
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
| **getNetworkRequest** | [GetNetworkRequest](GetNetworkRequest.md) |  | |

### Return type

[**Network**](Network.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The complete network (cities → stations → pairs) |  -  |
| **403** | Missing/invalid API key or unauthenticated request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getNetworkGet

> Network getNetworkGet(action)

Get the transport network (GET variant)

Same as POST but with the action passed as a query parameter. **Note:** as of September 2026 the server returned &#x60;403 Forbidden&#x60; for unauthenticated GET requests without the API key; with the key it works. Kept for completeness. 

### Example

```ts
import {
  Configuration,
  NetworkApi,
} from '';
import type { GetNetworkGetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new NetworkApi(config);

  const body = {
    // string
    action: action_example,
  } satisfies GetNetworkGetRequest;

  try {
    const data = await api.getNetworkGet(body);
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
| **action** | `string` |  | [Defaults to `&#39;get_cities_extended&#39;`] |

### Return type

[**Network**](Network.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The complete network payload |  -  |
| **403** | Missing/invalid API key or unauthenticated request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

