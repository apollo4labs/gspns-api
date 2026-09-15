# AccountAction200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Success** | Pointer to **bool** |  | [optional] 
**Msg** | Pointer to **string** |  | [optional] 
**Code** | Pointer to **int32** | Numeric error code (e.g. 3 &#x3D; unknown station). | [optional] 

## Methods

### NewAccountAction200Response

`func NewAccountAction200Response() *AccountAction200Response`

NewAccountAction200Response instantiates a new AccountAction200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccountAction200ResponseWithDefaults

`func NewAccountAction200ResponseWithDefaults() *AccountAction200Response`

NewAccountAction200ResponseWithDefaults instantiates a new AccountAction200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSuccess

`func (o *AccountAction200Response) GetSuccess() bool`

GetSuccess returns the Success field if non-nil, zero value otherwise.

### GetSuccessOk

`func (o *AccountAction200Response) GetSuccessOk() (*bool, bool)`

GetSuccessOk returns a tuple with the Success field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuccess

`func (o *AccountAction200Response) SetSuccess(v bool)`

SetSuccess sets Success field to given value.

### HasSuccess

`func (o *AccountAction200Response) HasSuccess() bool`

HasSuccess returns a boolean if a field has been set.

### GetMsg

`func (o *AccountAction200Response) GetMsg() string`

GetMsg returns the Msg field if non-nil, zero value otherwise.

### GetMsgOk

`func (o *AccountAction200Response) GetMsgOk() (*string, bool)`

GetMsgOk returns a tuple with the Msg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMsg

`func (o *AccountAction200Response) SetMsg(v string)`

SetMsg sets Msg field to given value.

### HasMsg

`func (o *AccountAction200Response) HasMsg() bool`

HasMsg returns a boolean if a field has been set.

### GetCode

`func (o *AccountAction200Response) GetCode() int32`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *AccountAction200Response) GetCodeOk() (*int32, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *AccountAction200Response) SetCode(v int32)`

SetCode sets Code field to given value.

### HasCode

`func (o *AccountAction200Response) HasCode() bool`

HasCode returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


