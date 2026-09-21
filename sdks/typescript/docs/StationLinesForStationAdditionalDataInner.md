
# StationLinesForStationAdditionalDataInner


## Properties

Name | Type
------------ | -------------
`lineNumberForDisplay` | string
`vehicleGroup` | string
`lineType` | string
`lineTypeColorActive` | string
`lineTypeColorInactive` | string

## Example

```typescript
import type { StationLinesForStationAdditionalDataInner } from ''

// TODO: Update the object below with actual values
const example = {
  "lineNumberForDisplay": 35,
  "vehicleGroup": 0,
  "lineType": 2,
  "lineTypeColorActive": #000000,
  "lineTypeColorInactive": #000000,
} satisfies StationLinesForStationAdditionalDataInner

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StationLinesForStationAdditionalDataInner
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


