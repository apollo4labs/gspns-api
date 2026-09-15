
# City

A city (municipality) in the GSPNS network.

## Properties

Name | Type
------------ | -------------
`id` | number
`name` | string
`gbname` | string
`defaultStation` | number
`coordinates` | [Coordinates](Coordinates.md)
`country` | [CityCountry](CityCountry.md)
`classes` | string
`stations` | Array&lt;number&gt;
`pairs` | Array&lt;number&gt;
`slugs` | string
`hasTrainStation` | boolean

## Example

```typescript
import type { City } from ''

// TODO: Update the object below with actual values
const example = {
  "id": 72,
  "name": Novi Sad,
  "gbname": ,
  "defaultStation": 7,
  "coordinates": null,
  "country": null,
  "classes": ,
  "stations": [6801,6548,6726,12883],
  "pairs": [72,76,1473,72],
  "slugs": novisad,
  "hasTrainStation": false,
} satisfies City

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as City
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


