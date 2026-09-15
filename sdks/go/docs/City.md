# City

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | City ID. Novi Sad &#x3D; 72. | 
**Name** | **string** | City name (UTF-8, may contain escaped characters). | 
**Gbname** | Pointer to **string** | Google Business / geocoding name override (often empty). | [optional] 
**DefaultStation** | **int32** | Default (central) station ID for the city. Novi Sad &#x3D; 7. | 
**Coordinates** | [**Coordinates**](Coordinates.md) |  | 
**Country** | [**CityCountry**](CityCountry.md) |  | 
**Classes** | Pointer to **string** | Pipe/format string of fare classes (usually empty in the raw payload). | [optional] 
**Stations** | **[]int32** | All station IDs belonging to the city. | 
**Pairs** | **[]int32** | Line-pair IDs per station (used for route reconstruction). | 
**Slugs** | **string** | URL/geo slug of the city. | 
**HasTrainStation** | **bool** | Whether the city has a railway station. | 

## Methods

### NewCity

`func NewCity(id int32, name string, defaultStation int32, coordinates Coordinates, country CityCountry, stations []int32, pairs []int32, slugs string, hasTrainStation bool, ) *City`

NewCity instantiates a new City object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCityWithDefaults

`func NewCityWithDefaults() *City`

NewCityWithDefaults instantiates a new City object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *City) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *City) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *City) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *City) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *City) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *City) SetName(v string)`

SetName sets Name field to given value.


### GetGbname

`func (o *City) GetGbname() string`

GetGbname returns the Gbname field if non-nil, zero value otherwise.

### GetGbnameOk

`func (o *City) GetGbnameOk() (*string, bool)`

GetGbnameOk returns a tuple with the Gbname field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGbname

`func (o *City) SetGbname(v string)`

SetGbname sets Gbname field to given value.

### HasGbname

`func (o *City) HasGbname() bool`

HasGbname returns a boolean if a field has been set.

### GetDefaultStation

`func (o *City) GetDefaultStation() int32`

GetDefaultStation returns the DefaultStation field if non-nil, zero value otherwise.

### GetDefaultStationOk

`func (o *City) GetDefaultStationOk() (*int32, bool)`

GetDefaultStationOk returns a tuple with the DefaultStation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultStation

`func (o *City) SetDefaultStation(v int32)`

SetDefaultStation sets DefaultStation field to given value.


### GetCoordinates

`func (o *City) GetCoordinates() Coordinates`

GetCoordinates returns the Coordinates field if non-nil, zero value otherwise.

### GetCoordinatesOk

`func (o *City) GetCoordinatesOk() (*Coordinates, bool)`

GetCoordinatesOk returns a tuple with the Coordinates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoordinates

`func (o *City) SetCoordinates(v Coordinates)`

SetCoordinates sets Coordinates field to given value.


### GetCountry

`func (o *City) GetCountry() CityCountry`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *City) GetCountryOk() (*CityCountry, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *City) SetCountry(v CityCountry)`

SetCountry sets Country field to given value.


### GetClasses

`func (o *City) GetClasses() string`

GetClasses returns the Classes field if non-nil, zero value otherwise.

### GetClassesOk

`func (o *City) GetClassesOk() (*string, bool)`

GetClassesOk returns a tuple with the Classes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClasses

`func (o *City) SetClasses(v string)`

SetClasses sets Classes field to given value.

### HasClasses

`func (o *City) HasClasses() bool`

HasClasses returns a boolean if a field has been set.

### GetStations

`func (o *City) GetStations() []int32`

GetStations returns the Stations field if non-nil, zero value otherwise.

### GetStationsOk

`func (o *City) GetStationsOk() (*[]int32, bool)`

GetStationsOk returns a tuple with the Stations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStations

`func (o *City) SetStations(v []int32)`

SetStations sets Stations field to given value.


### GetPairs

`func (o *City) GetPairs() []int32`

GetPairs returns the Pairs field if non-nil, zero value otherwise.

### GetPairsOk

`func (o *City) GetPairsOk() (*[]int32, bool)`

GetPairsOk returns a tuple with the Pairs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPairs

`func (o *City) SetPairs(v []int32)`

SetPairs sets Pairs field to given value.


### GetSlugs

`func (o *City) GetSlugs() string`

GetSlugs returns the Slugs field if non-nil, zero value otherwise.

### GetSlugsOk

`func (o *City) GetSlugsOk() (*string, bool)`

GetSlugsOk returns a tuple with the Slugs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlugs

`func (o *City) SetSlugs(v string)`

SetSlugs sets Slugs field to given value.


### GetHasTrainStation

`func (o *City) GetHasTrainStation() bool`

GetHasTrainStation returns the HasTrainStation field if non-nil, zero value otherwise.

### GetHasTrainStationOk

`func (o *City) GetHasTrainStationOk() (*bool, bool)`

GetHasTrainStationOk returns a tuple with the HasTrainStation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasTrainStation

`func (o *City) SetHasTrainStation(v bool)`

SetHasTrainStation sets HasTrainStation field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


