# City

A city (municipality) in the GSPNS network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | City ID. Novi Sad &#x3D; 72. | 
**name** | **str** | City name (UTF-8, may contain escaped characters). | 
**gbname** | **str** | Google Business / geocoding name override (often empty). | [optional] 
**default_station** | **int** | Default (central) station ID for the city. Novi Sad &#x3D; 7. | 
**coordinates** | [**Coordinates**](Coordinates.md) |  | 
**country** | [**CityCountry**](CityCountry.md) |  | 
**classes** | **str** | Pipe/format string of fare classes (usually empty in the raw payload). | [optional] 
**stations** | **List[int]** | All station IDs belonging to the city. | 
**pairs** | **List[int]** | Line-pair IDs per station (used for route reconstruction). | 
**slugs** | **str** | URL/geo slug of the city. | 
**has_train_station** | **bool** | Whether the city has a railway station. | 

## Example

```python
from jgsp_client.models.city import City

# TODO update the JSON string below
json = "{}"
# create an instance of City from a JSON string
city_instance = City.from_json(json)
# print the JSON string representation of the object
print(City.to_json())

# convert the object into a dict
city_dict = city_instance.to_dict()
# create an instance of City from a dict
city_from_dict = City.from_dict(city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


