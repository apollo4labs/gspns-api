
# StationCoordinates

Position. Unlike `City.coordinates`, the values are **strings** here.

## Properties

Name | Type
------------ | -------------
`latitude` | string
`longitude` | string

## Example

```typescript
import type { StationCoordinates } from ''

// TODO: Update the object below with actual values
const example = {
  "latitude": 45.3141430070,
  "longitude": 19.8293094486,
} satisfies StationCoordinates

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StationCoordinates
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


