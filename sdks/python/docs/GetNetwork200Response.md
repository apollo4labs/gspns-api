# GetNetwork200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cities** | [**List[City]**](City.md) | All cities in the network | 

## Example

```python
from jgsp_client.models.get_network200_response import GetNetwork200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetwork200Response from a JSON string
get_network200_response_instance = GetNetwork200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetwork200Response.to_json())

# convert the object into a dict
get_network200_response_dict = get_network200_response_instance.to_dict()
# create an instance of GetNetwork200Response from a dict
get_network200_response_from_dict = GetNetwork200Response.from_dict(get_network200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


