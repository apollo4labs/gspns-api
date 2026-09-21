# Station

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | Station ID — the value used as &#x60;station_uid&#x60; and in &#x60;Line.all_stations&#x60;. | 
**Name** | **string** |  | 
**StationId** | Pointer to **string** | Operator&#39;s own station code (not the numeric &#x60;id&#x60;). | [optional] 
**Slugs** | Pointer to **string** |  | [optional] 
**CityId** | **int32** |  | 
**CityName** | **string** |  | 
**Coordinates** | [**StationCoordinates**](StationCoordinates.md) |  | 
**Pairs** | Pointer to **[]int32** | Line-pair IDs serving the station (may contain repeats). | [optional] 
**ImportanceOrder** | Pointer to **int32** |  | [optional] 
**TrainStation** | Pointer to **bool** |  | [optional] 
**LinesForStation** | **[]string** | Display numbers of the lines that stop here. | 
**LinesForStationAdditionalData** | Pointer to [**[]StationLinesForStationAdditionalDataInner**](StationLinesForStationAdditionalDataInner.md) |  | [optional] 

## Methods

### NewStation

`func NewStation(id int32, name string, cityId int32, cityName string, coordinates StationCoordinates, linesForStation []string, ) *Station`

NewStation instantiates a new Station object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStationWithDefaults

`func NewStationWithDefaults() *Station`

NewStationWithDefaults instantiates a new Station object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Station) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Station) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Station) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *Station) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Station) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Station) SetName(v string)`

SetName sets Name field to given value.


### GetStationId

`func (o *Station) GetStationId() string`

GetStationId returns the StationId field if non-nil, zero value otherwise.

### GetStationIdOk

`func (o *Station) GetStationIdOk() (*string, bool)`

GetStationIdOk returns a tuple with the StationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStationId

`func (o *Station) SetStationId(v string)`

SetStationId sets StationId field to given value.

### HasStationId

`func (o *Station) HasStationId() bool`

HasStationId returns a boolean if a field has been set.

### GetSlugs

`func (o *Station) GetSlugs() string`

GetSlugs returns the Slugs field if non-nil, zero value otherwise.

### GetSlugsOk

`func (o *Station) GetSlugsOk() (*string, bool)`

GetSlugsOk returns a tuple with the Slugs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlugs

`func (o *Station) SetSlugs(v string)`

SetSlugs sets Slugs field to given value.

### HasSlugs

`func (o *Station) HasSlugs() bool`

HasSlugs returns a boolean if a field has been set.

### GetCityId

`func (o *Station) GetCityId() int32`

GetCityId returns the CityId field if non-nil, zero value otherwise.

### GetCityIdOk

`func (o *Station) GetCityIdOk() (*int32, bool)`

GetCityIdOk returns a tuple with the CityId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCityId

`func (o *Station) SetCityId(v int32)`

SetCityId sets CityId field to given value.


### GetCityName

`func (o *Station) GetCityName() string`

GetCityName returns the CityName field if non-nil, zero value otherwise.

### GetCityNameOk

`func (o *Station) GetCityNameOk() (*string, bool)`

GetCityNameOk returns a tuple with the CityName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCityName

`func (o *Station) SetCityName(v string)`

SetCityName sets CityName field to given value.


### GetCoordinates

`func (o *Station) GetCoordinates() StationCoordinates`

GetCoordinates returns the Coordinates field if non-nil, zero value otherwise.

### GetCoordinatesOk

`func (o *Station) GetCoordinatesOk() (*StationCoordinates, bool)`

GetCoordinatesOk returns a tuple with the Coordinates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoordinates

`func (o *Station) SetCoordinates(v StationCoordinates)`

SetCoordinates sets Coordinates field to given value.


### GetPairs

`func (o *Station) GetPairs() []int32`

GetPairs returns the Pairs field if non-nil, zero value otherwise.

### GetPairsOk

`func (o *Station) GetPairsOk() (*[]int32, bool)`

GetPairsOk returns a tuple with the Pairs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPairs

`func (o *Station) SetPairs(v []int32)`

SetPairs sets Pairs field to given value.

### HasPairs

`func (o *Station) HasPairs() bool`

HasPairs returns a boolean if a field has been set.

### GetImportanceOrder

`func (o *Station) GetImportanceOrder() int32`

GetImportanceOrder returns the ImportanceOrder field if non-nil, zero value otherwise.

### GetImportanceOrderOk

`func (o *Station) GetImportanceOrderOk() (*int32, bool)`

GetImportanceOrderOk returns a tuple with the ImportanceOrder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportanceOrder

`func (o *Station) SetImportanceOrder(v int32)`

SetImportanceOrder sets ImportanceOrder field to given value.

### HasImportanceOrder

`func (o *Station) HasImportanceOrder() bool`

HasImportanceOrder returns a boolean if a field has been set.

### GetTrainStation

`func (o *Station) GetTrainStation() bool`

GetTrainStation returns the TrainStation field if non-nil, zero value otherwise.

### GetTrainStationOk

`func (o *Station) GetTrainStationOk() (*bool, bool)`

GetTrainStationOk returns a tuple with the TrainStation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrainStation

`func (o *Station) SetTrainStation(v bool)`

SetTrainStation sets TrainStation field to given value.

### HasTrainStation

`func (o *Station) HasTrainStation() bool`

HasTrainStation returns a boolean if a field has been set.

### GetLinesForStation

`func (o *Station) GetLinesForStation() []string`

GetLinesForStation returns the LinesForStation field if non-nil, zero value otherwise.

### GetLinesForStationOk

`func (o *Station) GetLinesForStationOk() (*[]string, bool)`

GetLinesForStationOk returns a tuple with the LinesForStation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinesForStation

`func (o *Station) SetLinesForStation(v []string)`

SetLinesForStation sets LinesForStation field to given value.


### GetLinesForStationAdditionalData

`func (o *Station) GetLinesForStationAdditionalData() []StationLinesForStationAdditionalDataInner`

GetLinesForStationAdditionalData returns the LinesForStationAdditionalData field if non-nil, zero value otherwise.

### GetLinesForStationAdditionalDataOk

`func (o *Station) GetLinesForStationAdditionalDataOk() (*[]StationLinesForStationAdditionalDataInner, bool)`

GetLinesForStationAdditionalDataOk returns a tuple with the LinesForStationAdditionalData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinesForStationAdditionalData

`func (o *Station) SetLinesForStationAdditionalData(v []StationLinesForStationAdditionalDataInner)`

SetLinesForStationAdditionalData sets LinesForStationAdditionalData field to given value.

### HasLinesForStationAdditionalData

`func (o *Station) HasLinesForStationAdditionalData() bool`

HasLinesForStationAdditionalData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


