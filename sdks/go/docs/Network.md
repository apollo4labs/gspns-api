# Network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Cities** | [**[]City**](City.md) | All cities in the network | 
**Stations** | [**[]Station**](Station.md) | Every station of every city, with its lines. | 
**Lines** | [**[]Line**](Line.md) | Every line, one entry per direction variant. | 
**BikeSharing** | Pointer to [**NetworkBikeSharing**](NetworkBikeSharing.md) |  | [optional] 
**SmartParking** | Pointer to [**NetworkSmartParking**](NetworkSmartParking.md) |  | [optional] 

## Methods

### NewNetwork

`func NewNetwork(cities []City, stations []Station, lines []Line, ) *Network`

NewNetwork instantiates a new Network object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNetworkWithDefaults

`func NewNetworkWithDefaults() *Network`

NewNetworkWithDefaults instantiates a new Network object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCities

`func (o *Network) GetCities() []City`

GetCities returns the Cities field if non-nil, zero value otherwise.

### GetCitiesOk

`func (o *Network) GetCitiesOk() (*[]City, bool)`

GetCitiesOk returns a tuple with the Cities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCities

`func (o *Network) SetCities(v []City)`

SetCities sets Cities field to given value.


### GetStations

`func (o *Network) GetStations() []Station`

GetStations returns the Stations field if non-nil, zero value otherwise.

### GetStationsOk

`func (o *Network) GetStationsOk() (*[]Station, bool)`

GetStationsOk returns a tuple with the Stations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStations

`func (o *Network) SetStations(v []Station)`

SetStations sets Stations field to given value.


### GetLines

`func (o *Network) GetLines() []Line`

GetLines returns the Lines field if non-nil, zero value otherwise.

### GetLinesOk

`func (o *Network) GetLinesOk() (*[]Line, bool)`

GetLinesOk returns a tuple with the Lines field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLines

`func (o *Network) SetLines(v []Line)`

SetLines sets Lines field to given value.


### GetBikeSharing

`func (o *Network) GetBikeSharing() NetworkBikeSharing`

GetBikeSharing returns the BikeSharing field if non-nil, zero value otherwise.

### GetBikeSharingOk

`func (o *Network) GetBikeSharingOk() (*NetworkBikeSharing, bool)`

GetBikeSharingOk returns a tuple with the BikeSharing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBikeSharing

`func (o *Network) SetBikeSharing(v NetworkBikeSharing)`

SetBikeSharing sets BikeSharing field to given value.

### HasBikeSharing

`func (o *Network) HasBikeSharing() bool`

HasBikeSharing returns a boolean if a field has been set.

### GetSmartParking

`func (o *Network) GetSmartParking() NetworkSmartParking`

GetSmartParking returns the SmartParking field if non-nil, zero value otherwise.

### GetSmartParkingOk

`func (o *Network) GetSmartParkingOk() (*NetworkSmartParking, bool)`

GetSmartParkingOk returns a tuple with the SmartParking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSmartParking

`func (o *Network) SetSmartParking(v NetworkSmartParking)`

SetSmartParking sets SmartParking field to given value.

### HasSmartParking

`func (o *Network) HasSmartParking() bool`

HasSmartParking returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


