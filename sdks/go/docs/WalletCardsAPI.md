# \WalletCardsAPI

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddOrConnectCard**](WalletCardsAPI.md#AddOrConnectCard) | **Post** /publicapi/v1/rest_options/android_add_or_connect_card.php | Add or connect a transport card
[**AdditionalOptions**](WalletCardsAPI.md#AdditionalOptions) | **Post** /publicapi/v1/rest_options/android_additional_options.php | Additional card/ticket options
[**AdditionalSettings**](WalletCardsAPI.md#AdditionalSettings) | **Post** /publicapi/v1/rest_options/android_additional_settings.php | Additional settings
[**PrepaidCardsLog**](WalletCardsAPI.md#PrepaidCardsLog) | **Post** /publicapi/v1/rest_options/android_prepaid_cards_log_online.php | Prepaid card online log



## AddOrConnectCard

> ApiStatus AddOrConnectCard(ctx).Action(action).CardUid(cardUid).Execute()

Add or connect a transport card



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
	action := "action_example" // string | 
	cardUid := "cardUid_example" // string | UID of the physical card being connected. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WalletCardsAPI.AddOrConnectCard(context.Background()).Action(action).CardUid(cardUid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WalletCardsAPI.AddOrConnectCard``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddOrConnectCard`: ApiStatus
	fmt.Fprintf(os.Stdout, "Response from `WalletCardsAPI.AddOrConnectCard`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAddOrConnectCardRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **string** |  | 
 **cardUid** | **string** | UID of the physical card being connected. | 

### Return type

[**ApiStatus**](ApiStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AdditionalOptions

> []interface{} AdditionalOptions(ctx).Action(action).Execute()

Additional card/ticket options



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
	action := "action_example" // string | Option action verb.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WalletCardsAPI.AdditionalOptions(context.Background()).Action(action).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WalletCardsAPI.AdditionalOptions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AdditionalOptions`: []interface{}
	fmt.Fprintf(os.Stdout, "Response from `WalletCardsAPI.AdditionalOptions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAdditionalOptionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **string** | Option action verb. | 

### Return type

**[]interface{}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AdditionalSettings

> []interface{} AdditionalSettings(ctx).Action(action).Execute()

Additional settings



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
	action := "action_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WalletCardsAPI.AdditionalSettings(context.Background()).Action(action).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WalletCardsAPI.AdditionalSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AdditionalSettings`: []interface{}
	fmt.Fprintf(os.Stdout, "Response from `WalletCardsAPI.AdditionalSettings`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAdditionalSettingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **string** |  | 

### Return type

**[]interface{}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PrepaidCardsLog

> []interface{} PrepaidCardsLog(ctx).Action(action).Execute()

Prepaid card online log



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
	action := "action_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.WalletCardsAPI.PrepaidCardsLog(context.Background()).Action(action).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `WalletCardsAPI.PrepaidCardsLog``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PrepaidCardsLog`: []interface{}
	fmt.Fprintf(os.Stdout, "Response from `WalletCardsAPI.PrepaidCardsLog`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPrepaidCardsLogRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **string** |  | 

### Return type

**[]interface{}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

