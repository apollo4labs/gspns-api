# Station

A station (stop) from the network payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Station ID — the value used as &#x60;station_uid&#x60; and in &#x60;Line.all_stations&#x60;. | 
**name** | **str** |  | 
**station_id** | **str** | Operator&#39;s own station code (not the numeric &#x60;id&#x60;). | [optional] 
**slugs** | **str** |  | [optional] 
**city_id** | **int** |  | 
**city_name** | **str** |  | 
**coordinates** | [**StationCoordinates**](StationCoordinates.md) |  | 
**pairs** | **List[int]** | Line-pair IDs serving the station (may contain repeats). | [optional] 
**importance_order** | **int** |  | [optional] 
**train_station** | **bool** |  | [optional] 
**lines_for_station** | **List[str]** | Display numbers of the lines that stop here. | 
**lines_for_station_additional_data** | [**List[StationLinesForStationAdditionalDataInner]**](StationLinesForStationAdditionalDataInner.md) |  | [optional] 

## Example

```python
from jgsp_client.models.station import Station

# TODO update the JSON string below
json = "{}"
# create an instance of Station from a JSON string
station_instance = Station.from_json(json)
# print the JSON string representation of the object
print(Station.to_json())

# convert the object into a dict
station_dict = station_instance.to_dict()
# create an instance of Station from a dict
station_from_dict = Station.from_dict(station_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


