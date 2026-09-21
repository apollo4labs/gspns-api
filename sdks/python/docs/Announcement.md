# Announcement

Real-time prediction for one approaching vehicle at a station.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds_left** | **int** | Estimated seconds until the vehicle reaches this station. | 
**line_number** | **str** | Line code of the approaching vehicle. | 
**stations_gpsx** | **str** | Station latitude as string. | [optional] 
**stations_gpsy** | **str** | Station longitude as string. | [optional] 
**station_name** | **str** | Name of the queried station. | 
**actual_line_number** | **str** | Effective line code (same as line_number in practice). | 
**stations_between** | **int** | Number of stops the vehicle still has to call at *before* this station, so &#x60;0&#x60; means this station is its very next stop. If this station sits at index &#x60;t&#x60; in &#x60;all_stations&#x60;, the vehicle is heading for index &#x60;t - stations_between&#x60; (it is at or just past the stop before that). On loop lines, where the same station appears twice in &#x60;all_stations&#x60;, this is what tells the two passes apart: pick the occurrence whose &#x60;t - stations_between&#x60; entry lies nearest the vehicle.  | 
**garage_no** | **str** | Physical vehicle (garage) number. | 
**line_title** | **str** | Full route description of the line. | 
**main_line_title** | **str** | Main/alternate route description. | 
**vehicles** | [**List[VehiclePosition]**](VehiclePosition.md) | Live GPS positions of vehicles on this trip (usually one). | 
**all_stations** | [**List[AnnouncementAllStationsInner]**](AnnouncementAllStationsInner.md) | Complete ordered station sequence of the line with coordinates — the whole line, not only the part the vehicle still has to drive.  | 
**station_uid** | **int** | The queried station ID. | [optional] 

## Example

```python
from jgsp_client.models.announcement import Announcement

# TODO update the JSON string below
json = "{}"
# create an instance of Announcement from a JSON string
announcement_instance = Announcement.from_json(json)
# print the JSON string representation of the object
print(Announcement.to_json())

# convert the object into a dict
announcement_dict = announcement_instance.to_dict()
# create an instance of Announcement from a dict
announcement_from_dict = Announcement.from_dict(announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


