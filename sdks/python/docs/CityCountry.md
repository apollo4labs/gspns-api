# CityCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**alpha2_code** | **str** |  | 

## Example

```python
from jgsp_client.models.city_country import CityCountry

# TODO update the JSON string below
json = "{}"
# create an instance of CityCountry from a JSON string
city_country_instance = CityCountry.from_json(json)
# print the JSON string representation of the object
print(CityCountry.to_json())

# convert the object into a dict
city_country_dict = city_country_instance.to_dict()
# create an instance of CityCountry from a dict
city_country_from_dict = CityCountry.from_dict(city_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


