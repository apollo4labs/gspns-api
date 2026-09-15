
# CityCountry


## Properties

Name | Type
------------ | -------------
`name` | string
`alpha2Code` | string

## Example

```typescript
import type { CityCountry } from ''

// TODO: Update the object below with actual values
const example = {
  "name": Serbia,
  "alpha2Code": RS,
} satisfies CityCountry

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CityCountry
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


