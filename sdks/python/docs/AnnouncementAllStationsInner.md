# AnnouncementAllStationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**coordinates** | [**Coordinates**](Coordinates.md) |  | 

## Example

```python
from jgsp_client.models.announcement_all_stations_inner import AnnouncementAllStationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementAllStationsInner from a JSON string
announcement_all_stations_inner_instance = AnnouncementAllStationsInner.from_json(json)
# print the JSON string representation of the object
print(AnnouncementAllStationsInner.to_json())

# convert the object into a dict
announcement_all_stations_inner_dict = announcement_all_stations_inner_instance.to_dict()
# create an instance of AnnouncementAllStationsInner from a dict
announcement_all_stations_inner_from_dict = AnnouncementAllStationsInner.from_dict(announcement_all_stations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


