# GetNetworkGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cities** | [**List[City]**](City.md) |  | [optional] 

## Example

```python
from jgsp_client.models.get_network_get200_response import GetNetworkGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkGet200Response from a JSON string
get_network_get200_response_instance = GetNetworkGet200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkGet200Response.to_json())

# convert the object into a dict
get_network_get200_response_dict = get_network_get200_response_instance.to_dict()
# create an instance of GetNetworkGet200Response from a dict
get_network_get200_response_from_dict = GetNetworkGet200Response.from_dict(get_network_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


