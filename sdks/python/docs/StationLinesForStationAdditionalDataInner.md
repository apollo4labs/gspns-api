# StationLinesForStationAdditionalDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number_for_display** | **str** |  | [optional] 
**vehicle_group** | **str** |  | [optional] 
**line_type** | **str** | Line class — &#x60;1&#x60;, &#x60;2&#x60; or &#x60;3&#x60; (see &#x60;Line.line_type&#x60;). | [optional] 
**line_type_color_active** | **str** |  | [optional] 
**line_type_color_inactive** | **str** |  | [optional] 

## Example

```python
from jgsp_client.models.station_lines_for_station_additional_data_inner import StationLinesForStationAdditionalDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of StationLinesForStationAdditionalDataInner from a JSON string
station_lines_for_station_additional_data_inner_instance = StationLinesForStationAdditionalDataInner.from_json(json)
# print the JSON string representation of the object
print(StationLinesForStationAdditionalDataInner.to_json())

# convert the object into a dict
station_lines_for_station_additional_data_inner_dict = station_lines_for_station_additional_data_inner_instance.to_dict()
# create an instance of StationLinesForStationAdditionalDataInner from a dict
station_lines_for_station_additional_data_inner_from_dict = StationLinesForStationAdditionalDataInner.from_dict(station_lines_for_station_additional_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


