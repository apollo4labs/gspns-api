# GetNetworkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action verb. Observed values all return the same network payload. | [default to 'get_cities_extended']

## Example

```python
from jgsp_client.models.get_network_request import GetNetworkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkRequest from a JSON string
get_network_request_instance = GetNetworkRequest.from_json(json)
# print the JSON string representation of the object
print(GetNetworkRequest.to_json())

# convert the object into a dict
get_network_request_dict = get_network_request_instance.to_dict()
# create an instance of GetNetworkRequest from a dict
get_network_request_from_dict = GetNetworkRequest.from_dict(get_network_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


