# \PaymentsAPI

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AllsecurePayment**](PaymentsAPI.md#AllsecurePayment) | **Post** /publicapi/v1/rest_options/android_allsecure.php | AllSecure payment operations



## AllsecurePayment

> map[string]interface{} AllsecurePayment(ctx).Action(action).Execute()

AllSecure payment operations



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
	action := "action_example" // string | e.g. validate, finalize, check_status

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PaymentsAPI.AllsecurePayment(context.Background()).Action(action).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PaymentsAPI.AllsecurePayment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AllsecurePayment`: map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `PaymentsAPI.AllsecurePayment`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAllsecurePaymentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **string** | e.g. validate, finalize, check_status | 

### Return type

**map[string]interface{}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

