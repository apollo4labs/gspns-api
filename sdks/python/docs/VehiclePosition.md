# VehiclePosition

Live GPS position of a vehicle. A vehicle with no GPS fix is reported at `lat: \"0.00000000\"`, `lng: \"0.00000000\"` — treat that as \"unknown\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**garage_no** | **str** | Vehicle/garage number (can be an empty string). | 
**lat** | **str** | Latitude as string. | 
**lng** | **str** | Longitude as string. | 

## Example

```python
from jgsp_client.models.vehicle_position import VehiclePosition

# TODO update the JSON string below
json = "{}"
# create an instance of VehiclePosition from a JSON string
vehicle_position_instance = VehiclePosition.from_json(json)
# print the JSON string representation of the object
print(VehiclePosition.to_json())

# convert the object into a dict
vehicle_position_dict = vehicle_position_instance.to_dict()
# create an instance of VehiclePosition from a dict
vehicle_position_from_dict = VehiclePosition.from_dict(vehicle_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


