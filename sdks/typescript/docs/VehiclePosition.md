
# VehiclePosition

Live GPS position of a vehicle.

## Properties

Name | Type
------------ | -------------
`garageNo` | string
`lat` | string
`lng` | string

## Example

```typescript
import type { VehiclePosition } from ''

// TODO: Update the object below with actual values
const example = {
  "garageNo": 1102,
  "lat": 45.24890660,
  "lng": 19.79147330,
} satisfies VehiclePosition

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as VehiclePosition
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


