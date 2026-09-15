# Announcement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SecondsLeft** | **int32** | Estimated seconds until the vehicle reaches this station. | 
**LineNumber** | **string** | Line code of the approaching vehicle. | 
**StationsGpsx** | Pointer to **string** | Station latitude as string. | [optional] 
**StationsGpsy** | Pointer to **string** | Station longitude as string. | [optional] 
**StationName** | **string** | Name of the queried station. | 
**ActualLineNumber** | **string** | Effective line code (same as line_number in practice). | 
**StationsBetween** | **int32** | Number of stations between the vehicle&#39;s current position and this station. | 
**GarageNo** | **string** | Physical vehicle (garage) number. | 
**LineTitle** | **string** | Full route description of the line. | 
**MainLineTitle** | **string** | Main/alternate route description. | 
**Vehicles** | [**[]VehiclePosition**](VehiclePosition.md) | Live GPS positions of vehicles on this trip (usually one). | 
**AllStations** | [**[]AnnouncementAllStationsInner**](AnnouncementAllStationsInner.md) | Complete ordered station sequence of the line with coordinates. | 
**StationUid** | Pointer to **int32** | The queried station ID. | [optional] 

## Methods

### NewAnnouncement

`func NewAnnouncement(secondsLeft int32, lineNumber string, stationName string, actualLineNumber string, stationsBetween int32, garageNo string, lineTitle string, mainLineTitle string, vehicles []VehiclePosition, allStations []AnnouncementAllStationsInner, ) *Announcement`

NewAnnouncement instantiates a new Announcement object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAnnouncementWithDefaults

`func NewAnnouncementWithDefaults() *Announcement`

NewAnnouncementWithDefaults instantiates a new Announcement object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSecondsLeft

`func (o *Announcement) GetSecondsLeft() int32`

GetSecondsLeft returns the SecondsLeft field if non-nil, zero value otherwise.

### GetSecondsLeftOk

`func (o *Announcement) GetSecondsLeftOk() (*int32, bool)`

GetSecondsLeftOk returns a tuple with the SecondsLeft field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecondsLeft

`func (o *Announcement) SetSecondsLeft(v int32)`

SetSecondsLeft sets SecondsLeft field to given value.


### GetLineNumber

`func (o *Announcement) GetLineNumber() string`

GetLineNumber returns the LineNumber field if non-nil, zero value otherwise.

### GetLineNumberOk

`func (o *Announcement) GetLineNumberOk() (*string, bool)`

GetLineNumberOk returns a tuple with the LineNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineNumber

`func (o *Announcement) SetLineNumber(v string)`

SetLineNumber sets LineNumber field to given value.


### GetStationsGpsx

`func (o *Announcement) GetStationsGpsx() string`

GetStationsGpsx returns the StationsGpsx field if non-nil, zero value otherwise.

### GetStationsGpsxOk

`func (o *Announcement) GetStationsGpsxOk() (*string, bool)`

GetStationsGpsxOk returns a tuple with the StationsGpsx field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStationsGpsx

`func (o *Announcement) SetStationsGpsx(v string)`

SetStationsGpsx sets StationsGpsx field to given value.

### HasStationsGpsx

`func (o *Announcement) HasStationsGpsx() bool`

HasStationsGpsx returns a boolean if a field has been set.

### GetStationsGpsy

`func (o *Announcement) GetStationsGpsy() string`

GetStationsGpsy returns the StationsGpsy field if non-nil, zero value otherwise.

### GetStationsGpsyOk

`func (o *Announcement) GetStationsGpsyOk() (*string, bool)`

GetStationsGpsyOk returns a tuple with the StationsGpsy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStationsGpsy

`func (o *Announcement) SetStationsGpsy(v string)`

SetStationsGpsy sets StationsGpsy field to given value.

### HasStationsGpsy

`func (o *Announcement) HasStationsGpsy() bool`

HasStationsGpsy returns a boolean if a field has been set.

### GetStationName

`func (o *Announcement) GetStationName() string`

GetStationName returns the StationName field if non-nil, zero value otherwise.

### GetStationNameOk

`func (o *Announcement) GetStationNameOk() (*string, bool)`

GetStationNameOk returns a tuple with the StationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStationName

`func (o *Announcement) SetStationName(v string)`

SetStationName sets StationName field to given value.


### GetActualLineNumber

`func (o *Announcement) GetActualLineNumber() string`

GetActualLineNumber returns the ActualLineNumber field if non-nil, zero value otherwise.

### GetActualLineNumberOk

`func (o *Announcement) GetActualLineNumberOk() (*string, bool)`

GetActualLineNumberOk returns a tuple with the ActualLineNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualLineNumber

`func (o *Announcement) SetActualLineNumber(v string)`

SetActualLineNumber sets ActualLineNumber field to given value.


### GetStationsBetween

`func (o *Announcement) GetStationsBetween() int32`

GetStationsBetween returns the StationsBetween field if non-nil, zero value otherwise.

### GetStationsBetweenOk

`func (o *Announcement) GetStationsBetweenOk() (*int32, bool)`

GetStationsBetweenOk returns a tuple with the StationsBetween field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStationsBetween

`func (o *Announcement) SetStationsBetween(v int32)`

SetStationsBetween sets StationsBetween field to given value.


### GetGarageNo

`func (o *Announcement) GetGarageNo() string`

GetGarageNo returns the GarageNo field if non-nil, zero value otherwise.

### GetGarageNoOk

`func (o *Announcement) GetGarageNoOk() (*string, bool)`

GetGarageNoOk returns a tuple with the GarageNo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGarageNo

`func (o *Announcement) SetGarageNo(v string)`

SetGarageNo sets GarageNo field to given value.


### GetLineTitle

`func (o *Announcement) GetLineTitle() string`

GetLineTitle returns the LineTitle field if non-nil, zero value otherwise.

### GetLineTitleOk

`func (o *Announcement) GetLineTitleOk() (*string, bool)`

GetLineTitleOk returns a tuple with the LineTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineTitle

`func (o *Announcement) SetLineTitle(v string)`

SetLineTitle sets LineTitle field to given value.


### GetMainLineTitle

`func (o *Announcement) GetMainLineTitle() string`

GetMainLineTitle returns the MainLineTitle field if non-nil, zero value otherwise.

### GetMainLineTitleOk

`func (o *Announcement) GetMainLineTitleOk() (*string, bool)`

GetMainLineTitleOk returns a tuple with the MainLineTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMainLineTitle

`func (o *Announcement) SetMainLineTitle(v string)`

SetMainLineTitle sets MainLineTitle field to given value.


### GetVehicles

`func (o *Announcement) GetVehicles() []VehiclePosition`

GetVehicles returns the Vehicles field if non-nil, zero value otherwise.

### GetVehiclesOk

`func (o *Announcement) GetVehiclesOk() (*[]VehiclePosition, bool)`

GetVehiclesOk returns a tuple with the Vehicles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVehicles

`func (o *Announcement) SetVehicles(v []VehiclePosition)`

SetVehicles sets Vehicles field to given value.


### GetAllStations

`func (o *Announcement) GetAllStations() []AnnouncementAllStationsInner`

GetAllStations returns the AllStations field if non-nil, zero value otherwise.

### GetAllStationsOk

`func (o *Announcement) GetAllStationsOk() (*[]AnnouncementAllStationsInner, bool)`

GetAllStationsOk returns a tuple with the AllStations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllStations

`func (o *Announcement) SetAllStations(v []AnnouncementAllStationsInner)`

SetAllStations sets AllStations field to given value.


### GetStationUid

`func (o *Announcement) GetStationUid() int32`

GetStationUid returns the StationUid field if non-nil, zero value otherwise.

### GetStationUidOk

`func (o *Announcement) GetStationUidOk() (*int32, bool)`

GetStationUidOk returns a tuple with the StationUid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStationUid

`func (o *Announcement) SetStationUid(v int32)`

SetStationUid sets StationUid field to given value.

### HasStationUid

`func (o *Announcement) HasStationUid() bool`

HasStationUid returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


