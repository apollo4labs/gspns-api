# \NetworkAPI

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetNetwork**](NetworkAPI.md#GetNetwork) | **Post** /publicapi/v1/networkextended.php | Get the full transport network (cities with stations)
[**GetNetworkGet**](NetworkAPI.md#GetNetworkGet) | **Get** /publicapi/v1/networkextended.php | Get the transport network (GET variant)



## GetNetwork

> GetNetwork200Response GetNetwork(ctx).GetNetworkRequest(getNetworkRequest).Execute()

Get the full transport network (cities with stations)



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	getNetworkRequest := *openapiclient.NewGetNetworkRequest("Action_example") // GetNetworkRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NetworkAPI.GetNetwork(context.Background()).GetNetworkRequest(getNetworkRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NetworkAPI.GetNetwork``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNetwork`: GetNetwork200Response
	fmt.Fprintf(os.Stdout, "Response from `NetworkAPI.GetNetwork`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetNetworkRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **getNetworkRequest** | [**GetNetworkRequest**](GetNetworkRequest.md) |  | 

### Return type

[**GetNetwork200Response**](GetNetwork200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetNetworkGet

> GetNetworkGet200Response GetNetworkGet(ctx).Action(action).Execute()

Get the transport network (GET variant)



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	action := "action_example" // string |  (default to "get_cities_extended")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NetworkAPI.GetNetworkGet(context.Background()).Action(action).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NetworkAPI.GetNetworkGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNetworkGet`: GetNetworkGet200Response
	fmt.Fprintf(os.Stdout, "Response from `NetworkAPI.GetNetworkGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetNetworkGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **string** |  | [default to &quot;get_cities_extended&quot;]

### Return type

[**GetNetworkGet200Response**](GetNetworkGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

