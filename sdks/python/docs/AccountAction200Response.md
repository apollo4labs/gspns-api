# AccountAction200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**msg** | **str** |  | [optional] 
**code** | **int** | Numeric error code (e.g. 3 &#x3D; unknown station). | [optional] 

## Example

```python
from jgsp_client.models.account_action200_response import AccountAction200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAction200Response from a JSON string
account_action200_response_instance = AccountAction200Response.from_json(json)
# print the JSON string representation of the object
print(AccountAction200Response.to_json())

# convert the object into a dict
account_action200_response_dict = account_action200_response_instance.to_dict()
# create an instance of AccountAction200Response from a dict
account_action200_response_from_dict = AccountAction200Response.from_dict(account_action200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


