# Line

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**LineNumber** | **string** | Internal line code. | 
**LineNumberForDisplay** | **string** | Rider-facing line number. | 
**ActualLineNumber** | Pointer to **string** |  | [optional] 
**LineTitle** | **string** |  | 
**LineTitleForDisplay** | Pointer to **string** |  | [optional] 
**DirectionIdForDisplay** | Pointer to **string** |  | [optional] 
**PriceVariationId** | Pointer to **string** |  | [optional] 
**LineType** | Pointer to **string** | Line class (&#x60;1&#x60;, &#x60;2&#x60; or &#x60;3&#x60;). | [optional] 
**LineTypeColorActive** | Pointer to **string** |  | [optional] 
**LineTypeColorInactive** | Pointer to **string** |  | [optional] 
**AllStations** | **[]string** | Station IDs (as strings) in travel order, all legs concatenated. | 

## Methods

### NewLine

`func NewLine(id string, lineNumber string, lineNumberForDisplay string, lineTitle string, allStations []string, ) *Line`

NewLine instantiates a new Line object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLineWithDefaults

`func NewLineWithDefaults() *Line`

NewLineWithDefaults instantiates a new Line object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Line) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Line) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Line) SetId(v string)`

SetId sets Id field to given value.


### GetLineNumber

`func (o *Line) GetLineNumber() string`

GetLineNumber returns the LineNumber field if non-nil, zero value otherwise.

### GetLineNumberOk

`func (o *Line) GetLineNumberOk() (*string, bool)`

GetLineNumberOk returns a tuple with the LineNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineNumber

`func (o *Line) SetLineNumber(v string)`

SetLineNumber sets LineNumber field to given value.


### GetLineNumberForDisplay

`func (o *Line) GetLineNumberForDisplay() string`

GetLineNumberForDisplay returns the LineNumberForDisplay field if non-nil, zero value otherwise.

### GetLineNumberForDisplayOk

`func (o *Line) GetLineNumberForDisplayOk() (*string, bool)`

GetLineNumberForDisplayOk returns a tuple with the LineNumberForDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineNumberForDisplay

`func (o *Line) SetLineNumberForDisplay(v string)`

SetLineNumberForDisplay sets LineNumberForDisplay field to given value.


### GetActualLineNumber

`func (o *Line) GetActualLineNumber() string`

GetActualLineNumber returns the ActualLineNumber field if non-nil, zero value otherwise.

### GetActualLineNumberOk

`func (o *Line) GetActualLineNumberOk() (*string, bool)`

GetActualLineNumberOk returns a tuple with the ActualLineNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActualLineNumber

`func (o *Line) SetActualLineNumber(v string)`

SetActualLineNumber sets ActualLineNumber field to given value.

### HasActualLineNumber

`func (o *Line) HasActualLineNumber() bool`

HasActualLineNumber returns a boolean if a field has been set.

### GetLineTitle

`func (o *Line) GetLineTitle() string`

GetLineTitle returns the LineTitle field if non-nil, zero value otherwise.

### GetLineTitleOk

`func (o *Line) GetLineTitleOk() (*string, bool)`

GetLineTitleOk returns a tuple with the LineTitle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineTitle

`func (o *Line) SetLineTitle(v string)`

SetLineTitle sets LineTitle field to given value.


### GetLineTitleForDisplay

`func (o *Line) GetLineTitleForDisplay() string`

GetLineTitleForDisplay returns the LineTitleForDisplay field if non-nil, zero value otherwise.

### GetLineTitleForDisplayOk

`func (o *Line) GetLineTitleForDisplayOk() (*string, bool)`

GetLineTitleForDisplayOk returns a tuple with the LineTitleForDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineTitleForDisplay

`func (o *Line) SetLineTitleForDisplay(v string)`

SetLineTitleForDisplay sets LineTitleForDisplay field to given value.

### HasLineTitleForDisplay

`func (o *Line) HasLineTitleForDisplay() bool`

HasLineTitleForDisplay returns a boolean if a field has been set.

### GetDirectionIdForDisplay

`func (o *Line) GetDirectionIdForDisplay() string`

GetDirectionIdForDisplay returns the DirectionIdForDisplay field if non-nil, zero value otherwise.

### GetDirectionIdForDisplayOk

`func (o *Line) GetDirectionIdForDisplayOk() (*string, bool)`

GetDirectionIdForDisplayOk returns a tuple with the DirectionIdForDisplay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDirectionIdForDisplay

`func (o *Line) SetDirectionIdForDisplay(v string)`

SetDirectionIdForDisplay sets DirectionIdForDisplay field to given value.

### HasDirectionIdForDisplay

`func (o *Line) HasDirectionIdForDisplay() bool`

HasDirectionIdForDisplay returns a boolean if a field has been set.

### GetPriceVariationId

`func (o *Line) GetPriceVariationId() string`

GetPriceVariationId returns the PriceVariationId field if non-nil, zero value otherwise.

### GetPriceVariationIdOk

`func (o *Line) GetPriceVariationIdOk() (*string, bool)`

GetPriceVariationIdOk returns a tuple with the PriceVariationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriceVariationId

`func (o *Line) SetPriceVariationId(v string)`

SetPriceVariationId sets PriceVariationId field to given value.

### HasPriceVariationId

`func (o *Line) HasPriceVariationId() bool`

HasPriceVariationId returns a boolean if a field has been set.

### GetLineType

`func (o *Line) GetLineType() string`

GetLineType returns the LineType field if non-nil, zero value otherwise.

### GetLineTypeOk

`func (o *Line) GetLineTypeOk() (*string, bool)`

GetLineTypeOk returns a tuple with the LineType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineType

`func (o *Line) SetLineType(v string)`

SetLineType sets LineType field to given value.

### HasLineType

`func (o *Line) HasLineType() bool`

HasLineType returns a boolean if a field has been set.

### GetLineTypeColorActive

`func (o *Line) GetLineTypeColorActive() string`

GetLineTypeColorActive returns the LineTypeColorActive field if non-nil, zero value otherwise.

### GetLineTypeColorActiveOk

`func (o *Line) GetLineTypeColorActiveOk() (*string, bool)`

GetLineTypeColorActiveOk returns a tuple with the LineTypeColorActive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineTypeColorActive

`func (o *Line) SetLineTypeColorActive(v string)`

SetLineTypeColorActive sets LineTypeColorActive field to given value.

### HasLineTypeColorActive

`func (o *Line) HasLineTypeColorActive() bool`

HasLineTypeColorActive returns a boolean if a field has been set.

### GetLineTypeColorInactive

`func (o *Line) GetLineTypeColorInactive() string`

GetLineTypeColorInactive returns the LineTypeColorInactive field if non-nil, zero value otherwise.

### GetLineTypeColorInactiveOk

`func (o *Line) GetLineTypeColorInactiveOk() (*string, bool)`

GetLineTypeColorInactiveOk returns a tuple with the LineTypeColorInactive field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLineTypeColorInactive

`func (o *Line) SetLineTypeColorInactive(v string)`

SetLineTypeColorInactive sets LineTypeColorInactive field to given value.

### HasLineTypeColorInactive

`func (o *Line) HasLineTypeColorInactive() bool`

HasLineTypeColorInactive returns a boolean if a field has been set.

### GetAllStations

`func (o *Line) GetAllStations() []string`

GetAllStations returns the AllStations field if non-nil, zero value otherwise.

### GetAllStationsOk

`func (o *Line) GetAllStationsOk() (*[]string, bool)`

GetAllStationsOk returns a tuple with the AllStations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllStations

`func (o *Line) SetAllStations(v []string)`

SetAllStations sets AllStations field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


