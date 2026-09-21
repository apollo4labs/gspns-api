# NetworkBikeSharing

Bike-sharing pylons; the list is empty for Novi Sad.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pylons** | **List[object]** |  | [optional] 

## Example

```python
from jgsp_client.models.network_bike_sharing import NetworkBikeSharing

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBikeSharing from a JSON string
network_bike_sharing_instance = NetworkBikeSharing.from_json(json)
# print the JSON string representation of the object
print(NetworkBikeSharing.to_json())

# convert the object into a dict
network_bike_sharing_dict = network_bike_sharing_instance.to_dict()
# create an instance of NetworkBikeSharing from a dict
network_bike_sharing_from_dict = NetworkBikeSharing.from_dict(network_bike_sharing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


