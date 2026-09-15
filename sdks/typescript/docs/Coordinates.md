
# Coordinates

Geographic coordinates. Values are numbers (cities) or strings (stations).

## Properties

Name | Type
------------ | -------------
`latitude` | [CoordinatesLatitude](CoordinatesLatitude.md)
`longitude` | [CoordinatesLongitude](CoordinatesLongitude.md)

## Example

```typescript
import type { Coordinates } from ''

// TODO: Update the object below with actual values
const example = {
  "latitude": null,
  "longitude": null,
} satisfies Coordinates

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Coordinates
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


