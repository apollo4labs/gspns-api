# Coordinates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Latitude** | Pointer to [**CoordinatesLatitude**](CoordinatesLatitude.md) |  | [optional] 
**Longitude** | Pointer to [**CoordinatesLongitude**](CoordinatesLongitude.md) |  | [optional] 

## Methods

### NewCoordinates

`func NewCoordinates() *Coordinates`

NewCoordinates instantiates a new Coordinates object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCoordinatesWithDefaults

`func NewCoordinatesWithDefaults() *Coordinates`

NewCoordinatesWithDefaults instantiates a new Coordinates object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLatitude

`func (o *Coordinates) GetLatitude() CoordinatesLatitude`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *Coordinates) GetLatitudeOk() (*CoordinatesLatitude, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLatitude

`func (o *Coordinates) SetLatitude(v CoordinatesLatitude)`

SetLatitude sets Latitude field to given value.

### HasLatitude

`func (o *Coordinates) HasLatitude() bool`

HasLatitude returns a boolean if a field has been set.

### GetLongitude

`func (o *Coordinates) GetLongitude() CoordinatesLongitude`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *Coordinates) GetLongitudeOk() (*CoordinatesLongitude, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLongitude

`func (o *Coordinates) SetLongitude(v CoordinatesLongitude)`

SetLongitude sets Longitude field to given value.

### HasLongitude

`func (o *Coordinates) HasLongitude() bool`

HasLongitude returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


