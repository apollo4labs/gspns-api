# NetworkSmartParking

Smart-parking sensors; the list is empty for Novi Sad.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parking_sensors** | **List[object]** |  | [optional] 

## Example

```python
from jgsp_client.models.network_smart_parking import NetworkSmartParking

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSmartParking from a JSON string
network_smart_parking_instance = NetworkSmartParking.from_json(json)
# print the JSON string representation of the object
print(NetworkSmartParking.to_json())

# convert the object into a dict
network_smart_parking_dict = network_smart_parking_instance.to_dict()
# create an instance of NetworkSmartParking from a dict
network_smart_parking_from_dict = NetworkSmartParking.from_dict(network_smart_parking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


