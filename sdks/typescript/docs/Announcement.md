
# Announcement

Real-time prediction for one approaching vehicle at a station.

## Properties

Name | Type
------------ | -------------
`secondsLeft` | number
`lineNumber` | string
`stationsGpsx` | string
`stationsGpsy` | string
`stationName` | string
`actualLineNumber` | string
`stationsBetween` | number
`garageNo` | string
`lineTitle` | string
`mainLineTitle` | string
`vehicles` | [Array&lt;VehiclePosition&gt;](VehiclePosition.md)
`allStations` | [Array&lt;AnnouncementAllStationsInner&gt;](AnnouncementAllStationsInner.md)
`stationUid` | number

## Example

```typescript
import type { Announcement } from ''

// TODO: Update the object below with actual values
const example = {
  "secondsLeft": 1670,
  "lineNumber": 7A,
  "stationsGpsx": 45.2401130864,
  "stationsGpsy": 19.8370251247,
  "stationName": Narodnog fronta-Šekspirova,
  "actualLineNumber": 7A,
  "stationsBetween": 17,
  "garageNo": 1102,
  "lineTitle": NOVO NASELJE - ŽELEZNIČKA STANICA - FUTOŠKA PIJACA - LIMAN 4 - NOVO NASELJE,
  "mainLineTitle": NOVO NASELJE - ŽELEZNIČKA STANICA - FUTOŠKA PIJACA - LIMAN 4 - NOVO NASELJE,
  "vehicles": null,
  "allStations": null,
  "stationUid": 6532,
} satisfies Announcement

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Announcement
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


