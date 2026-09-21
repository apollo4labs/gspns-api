
# Network

Payload of `networkextended.php`. Besides `cities`, it carries the flat station and line lists (about 1000 stations and 100 lines for Novi Sad and its suburbs at the time of writing). 

## Properties

Name | Type
------------ | -------------
`cities` | [Array&lt;City&gt;](City.md)
`stations` | [Array&lt;Station&gt;](Station.md)
`lines` | [Array&lt;Line&gt;](Line.md)
`bikeSharing` | [NetworkBikeSharing](NetworkBikeSharing.md)
`smartParking` | [NetworkSmartParking](NetworkSmartParking.md)

## Example

```typescript
import type { Network } from ''

// TODO: Update the object below with actual values
const example = {
  "cities": null,
  "stations": null,
  "lines": null,
  "bikeSharing": null,
  "smartParking": null,
} satisfies Network

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Network
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


