# jgsp_client.RealtimeApi

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_station_announcements**](RealtimeApi.md#get_station_announcements) | **GET** /publicapi/v1/announcement/announcement.php | Get live arrivals &amp; vehicle positions for a station


# **get_station_announcements**
> List[Announcement] get_station_announcements(ibfm, station_uid)

Get live arrivals & vehicle positions for a station

Returns real-time departure/arrival predictions for every upcoming vehicle at the
given station. Each entry describes one approaching vehicle: seconds left until it
reaches the station, its current GPS position, how many stations away it is, the
garage (vehicle) number, and the full station sequence of its line.

Use `ibfm=TM00000` for all lines, or a specific line code (e.g. `7A`) to filter.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import jgsp_client
from jgsp_client.models.announcement import Announcement
from jgsp_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://online.nsmart.rs
# See configuration.py for a list of all supported configuration parameters.
configuration = jgsp_client.Configuration(
    host = "https://online.nsmart.rs"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with jgsp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jgsp_client.RealtimeApi(api_client)
    ibfm = 'TM00000' # str | Line filter. `TM00000` = all lines; otherwise a line code such as `7A` or `8`. (default to 'TM00000')
    station_uid = 6532 # int | Station ID (see network endpoint for the full station list). E.g. 6532 = \"Narodnog fronta-Šekspirova\".

    try:
        # Get live arrivals & vehicle positions for a station
        api_response = api_instance.get_station_announcements(ibfm, station_uid)
        print("The response of RealtimeApi->get_station_announcements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealtimeApi->get_station_announcements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ibfm** | **str**| Line filter. &#x60;TM00000&#x60; &#x3D; all lines; otherwise a line code such as &#x60;7A&#x60; or &#x60;8&#x60;. | [default to &#39;TM00000&#39;]
 **station_uid** | **int**| Station ID (see network endpoint for the full station list). E.g. 6532 &#x3D; \&quot;Narodnog fronta-Šekspirova\&quot;. | 

### Return type

[**List[Announcement]**](Announcement.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of approaching vehicles with predictions. For an unknown/invalid station_uid the server returns an error array instead: &#x60;[{\&quot;success\&quot;:false,\&quot;code\&quot;:3}]&#x60;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

