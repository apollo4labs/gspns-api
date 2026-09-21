# VehiclePosition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GarageNo** | **string** | Vehicle/garage number (can be an empty string). | 
**Lat** | **string** | Latitude as string. | 
**Lng** | **string** | Longitude as string. | 

## Methods

### NewVehiclePosition

`func NewVehiclePosition(garageNo string, lat string, lng string, ) *VehiclePosition`

NewVehiclePosition instantiates a new VehiclePosition object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVehiclePositionWithDefaults

`func NewVehiclePositionWithDefaults() *VehiclePosition`

NewVehiclePositionWithDefaults instantiates a new VehiclePosition object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGarageNo

`func (o *VehiclePosition) GetGarageNo() string`

GetGarageNo returns the GarageNo field if non-nil, zero value otherwise.

### GetGarageNoOk

`func (o *VehiclePosition) GetGarageNoOk() (*string, bool)`

GetGarageNoOk returns a tuple with the GarageNo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGarageNo

`func (o *VehiclePosition) SetGarageNo(v string)`

SetGarageNo sets GarageNo field to given value.


### GetLat

`func (o *VehiclePosition) GetLat() string`

GetLat returns the Lat field if non-nil, zero value otherwise.

### GetLatOk

`func (o *VehiclePosition) GetLatOk() (*string, bool)`

GetLatOk returns a tuple with the Lat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLat

`func (o *VehiclePosition) SetLat(v string)`

SetLat sets Lat field to given value.


### GetLng

`func (o *VehiclePosition) GetLng() string`

GetLng returns the Lng field if non-nil, zero value otherwise.

### GetLngOk

`func (o *VehiclePosition) GetLngOk() (*string, bool)`

GetLngOk returns a tuple with the Lng field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLng

`func (o *VehiclePosition) SetLng(v string)`

SetLng sets Lng field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


