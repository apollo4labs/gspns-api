# StationCoordinates

Position. Unlike `City.coordinates`, the values are **strings** here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **str** |  | 
**longitude** | **str** |  | 

## Example

```python
from jgsp_client.models.station_coordinates import StationCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of StationCoordinates from a JSON string
station_coordinates_instance = StationCoordinates.from_json(json)
# print the JSON string representation of the object
print(StationCoordinates.to_json())

# convert the object into a dict
station_coordinates_dict = station_coordinates_instance.to_dict()
# create an instance of StationCoordinates from a dict
station_coordinates_from_dict = StationCoordinates.from_dict(station_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


