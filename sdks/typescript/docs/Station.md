
# Station

A station (stop) from the network payload.

## Properties

Name | Type
------------ | -------------
`id` | number
`name` | string
`stationId` | string
`slugs` | string
`cityId` | number
`cityName` | string
`coordinates` | [StationCoordinates](StationCoordinates.md)
`pairs` | Array&lt;number&gt;
`importanceOrder` | number
`trainStation` | boolean
`linesForStation` | Array&lt;string&gt;
`linesForStationAdditionalData` | [Array&lt;StationLinesForStationAdditionalDataInner&gt;](StationLinesForStationAdditionalDataInner.md)

## Example

```typescript
import type { Station } from ''

// TODO: Update the object below with actual values
const example = {
  "id": 6801,
  "name": Agrovojvodina,
  "stationId": 0125PB,
  "slugs": null,
  "cityId": 72,
  "cityName": Novi Sad,
  "coordinates": null,
  "pairs": null,
  "importanceOrder": null,
  "trainStation": null,
  "linesForStation": ["35","35ČL","35L"],
  "linesForStationAdditionalData": null,
} satisfies Station

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Station
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


