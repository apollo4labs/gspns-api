# \RealtimeAPI

All URIs are relative to *https://online.nsmart.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetStationAnnouncements**](RealtimeAPI.md#GetStationAnnouncements) | **Get** /publicapi/v1/announcement/announcement.php | Get live arrivals &amp; vehicle positions for a station



## GetStationAnnouncements

> []Announcement GetStationAnnouncements(ctx).Ibfm(ibfm).StationUid(stationUid).Execute()

Get live arrivals & vehicle positions for a station



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	ibfm := "TM00000" // string | Line filter. `TM00000` = all lines; otherwise a line code such as `7A` or `8`. (default to "TM00000")
	stationUid := int32(6532) // int32 | Station ID (see network endpoint for the full station list). E.g. 6532 = \"Narodnog fronta-Šekspirova\".

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RealtimeAPI.GetStationAnnouncements(context.Background()).Ibfm(ibfm).StationUid(stationUid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RealtimeAPI.GetStationAnnouncements``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetStationAnnouncements`: []Announcement
	fmt.Fprintf(os.Stdout, "Response from `RealtimeAPI.GetStationAnnouncements`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetStationAnnouncementsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ibfm** | **string** | Line filter. &#x60;TM00000&#x60; &#x3D; all lines; otherwise a line code such as &#x60;7A&#x60; or &#x60;8&#x60;. | [default to &quot;TM00000&quot;]
 **stationUid** | **int32** | Station ID (see network endpoint for the full station list). E.g. 6532 &#x3D; \&quot;Narodnog fronta-Šekspirova\&quot;. | 

### Return type

[**[]Announcement**](Announcement.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

