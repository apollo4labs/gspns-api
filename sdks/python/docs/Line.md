# Line

A line (one direction variant) from the network payload.  * `line_number_for_display` is the number riders know (\"1\", \"7A\") and is unique per   entry. `line_number` / `actual_line_number` are the operator's internal codes and can   differ from it (internal `10` is displayed as `1`, internal `41` as `10`, `101` as   `10APT`) — use the display number when talking to riders, and match on it against   `announcement.php`'s `line_number`. * `all_stations` is every leg of the line **concatenated** (outbound, branch   variants and the return trip) — it is not a single one-way path. Return legs mostly   use their own stop IDs, so the list does not repeat IDs at the turnaround. * A few stop IDs in `all_stations` are not present in `Network.stations`; skip them. * `line_type_color_active` was `#000000` for every line when checked, so it carries   no usable line color. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**line_number** | **str** | Internal line code. | 
**line_number_for_display** | **str** | Rider-facing line number. | 
**actual_line_number** | **str** |  | [optional] 
**line_title** | **str** |  | 
**line_title_for_display** | **str** |  | [optional] 
**direction_id_for_display** | **str** |  | [optional] 
**price_variation_id** | **str** |  | [optional] 
**line_type** | **str** | Line class (&#x60;1&#x60;, &#x60;2&#x60; or &#x60;3&#x60;). | [optional] 
**line_type_color_active** | **str** |  | [optional] 
**line_type_color_inactive** | **str** |  | [optional] 
**all_stations** | **List[str]** | Station IDs (as strings) in travel order, all legs concatenated. | 

## Example

```python
from jgsp_client.models.line import Line

# TODO update the JSON string below
json = "{}"
# create an instance of Line from a JSON string
line_instance = Line.from_json(json)
# print the JSON string representation of the object
print(Line.to_json())

# convert the object into a dict
line_dict = line_instance.to_dict()
# create an instance of Line from a dict
line_from_dict = Line.from_dict(line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


