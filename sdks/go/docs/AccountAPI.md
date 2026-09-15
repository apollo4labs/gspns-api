# \AccountAPI

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AccountAction**](AccountAPI.md#AccountAction) | **Post** /publicapi/v1/rest_options/android_login.php | Account actions (login, register, reset password…)



## AccountAction

> AccountAction200Response AccountAction(ctx).Action(action).Email(email).Password(password).FirstName(firstName).LastName(lastName).Execute()

Account actions (login, register, reset password…)



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
	action := "action_example" // string | Account action verb.
	email := "email_example" // string | Used by login/register/reset flows. (optional)
	password := "password_example" // string |  (optional)
	firstName := "firstName_example" // string |  (optional)
	lastName := "lastName_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AccountAPI.AccountAction(context.Background()).Action(action).Email(email).Password(password).FirstName(firstName).LastName(lastName).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AccountAPI.AccountAction``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AccountAction`: AccountAction200Response
	fmt.Fprintf(os.Stdout, "Response from `AccountAPI.AccountAction`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAccountActionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **string** | Account action verb. | 
 **email** | **string** | Used by login/register/reset flows. | 
 **password** | **string** |  | 
 **firstName** | **string** |  | 
 **lastName** | **string** |  | 

### Return type

[**AccountAction200Response**](AccountAction200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

