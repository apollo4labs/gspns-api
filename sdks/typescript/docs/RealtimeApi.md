# RealtimeApi

All URIs are relative to *https://online.nsmart.rs*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStationAnnouncements**](RealtimeApi.md#getstationannouncements) | **GET** /publicapi/v1/announcement/announcement.php | Get live arrivals &amp; vehicle positions for a station |



## getStationAnnouncements

> Array&lt;Announcement&gt; getStationAnnouncements(ibfm, stationUid)

Get live arrivals &amp; vehicle positions for a station

Returns real-time departure/arrival predictions for every upcoming vehicle at the given station. Each entry describes one approaching vehicle: seconds left until it reaches the station, its current GPS position, how many stations away it is, the garage (vehicle) number, and the full station sequence of its line.  Use &#x60;ibfm&#x3D;TM00000&#x60; for all lines, or a specific line code (e.g. &#x60;7A&#x60;) to filter. 

### Example

```ts
import {
  Configuration,
  RealtimeApi,
} from '';
import type { GetStationAnnouncementsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new RealtimeApi(config);

  const body = {
    // string | Line filter. `TM00000` = all lines; otherwise a line code such as `7A` or `8`.
    ibfm: TM00000,
    // number | Station ID (see network endpoint for the full station list). E.g. 6532 = \"Narodnog fronta-Šekspirova\".
    stationUid: 6532,
  } satisfies GetStationAnnouncementsRequest;

  try {
    const data = await api.getStationAnnouncements(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ibfm** | `string` | Line filter. &#x60;TM00000&#x60; &#x3D; all lines; otherwise a line code such as &#x60;7A&#x60; or &#x60;8&#x60;. | [Defaults to `&#39;TM00000&#39;`] |
| **stationUid** | `number` | Station ID (see network endpoint for the full station list). E.g. 6532 &#x3D; \&quot;Narodnog fronta-Šekspirova\&quot;. | [Defaults to `undefined`] |

### Return type

[**Array&lt;Announcement&gt;**](Announcement.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of approaching vehicles with predictions. For an unknown/invalid station_uid the server returns an error array instead: &#x60;[{\&quot;success\&quot;:false,\&quot;code\&quot;:3}]&#x60;.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

