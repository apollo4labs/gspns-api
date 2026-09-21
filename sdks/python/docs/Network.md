# Network

Payload of `networkextended.php`. Besides `cities`, it carries the flat station and line lists (about 1000 stations and 100 lines for Novi Sad and its suburbs at the time of writing). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cities** | [**List[City]**](City.md) | All cities in the network | 
**stations** | [**List[Station]**](Station.md) | Every station of every city, with its lines. | 
**lines** | [**List[Line]**](Line.md) | Every line, one entry per direction variant. | 
**bike_sharing** | [**NetworkBikeSharing**](NetworkBikeSharing.md) |  | [optional] 
**smart_parking** | [**NetworkSmartParking**](NetworkSmartParking.md) |  | [optional] 

## Example

```python
from jgsp_client.models.network import Network

# TODO update the JSON string below
json = "{}"
# create an instance of Network from a JSON string
network_instance = Network.from_json(json)
# print the JSON string representation of the object
print(Network.to_json())

# convert the object into a dict
network_dict = network_instance.to_dict()
# create an instance of Network from a dict
network_from_dict = Network.from_dict(network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


