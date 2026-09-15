# AccountApi

All URIs are relative to *https://online.nsmart.rs*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountAction**](AccountApi.md#accountaction) | **POST** /publicapi/v1/rest_options/android_login.php | Account actions (login, register, reset password…) |



## accountAction

> AccountAction200Response accountAction(action, email, password, firstName, lastName)

Account actions (login, register, reset password…)

Single dispatcher endpoint for account-related actions, selected via the &#x60;action&#x60; form parameter. Observed behaviours (September 2026):  * &#x60;action&#x3D;register&#x60; → &#x60;{\&quot;success\&quot;:false,\&quot;msg\&quot;:\&quot;SIGNUP_FORM_NOT_CONFIGURED\&quot;}&#x60; (registration disabled for this operator) * &#x60;action&#x3D;login&#x60; and most other verbs → &#x60;[]&#x60; (empty array) * missing &#x60;action&#x60; → plain text &#x60;POTREBAN JE PARAMETAR ACTION&#x60; (\&quot;ACTION parameter is required\&quot;)  The full set of actions is not publicly documented; the NSmart APK shows login, register, social login (Google/Facebook), reset password and email verification flows. 

### Example

```ts
import {
  Configuration,
  AccountApi,
} from '';
import type { AccountActionRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new AccountApi(config);

  const body = {
    // string | Account action verb.
    action: action_example,
    // string | Used by login/register/reset flows. (optional)
    email: email_example,
    // string (optional)
    password: password_example,
    // string (optional)
    firstName: firstName_example,
    // string (optional)
    lastName: lastName_example,
  } satisfies AccountActionRequest;

  try {
    const data = await api.accountAction(body);
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
| **action** | `login`, `register`, `reset_password`, `verify_email` | Account action verb. | [Defaults to `undefined`] [Enum: login, register, reset_password, verify_email] |
| **email** | `string` | Used by login/register/reset flows. | [Optional] [Defaults to `undefined`] |
| **password** | `string` |  | [Optional] [Defaults to `undefined`] |
| **firstName** | `string` |  | [Optional] [Defaults to `undefined`] |
| **lastName** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**AccountAction200Response**](AccountAction200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/x-www-form-urlencoded`
- **Accept**: `application/json`, `text/plain`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Action-dependent result (array or status object) |  -  |
| **400** | Missing action parameter (plain text, not JSON) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

