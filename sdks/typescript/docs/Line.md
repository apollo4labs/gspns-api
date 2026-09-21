
# Line

A line (one direction variant) from the network payload.  * `line_number_for_display` is the number riders know (\"1\", \"7A\") and is unique per   entry. `line_number` / `actual_line_number` are the operator\'s internal codes and can   differ from it (internal `10` is displayed as `1`, internal `41` as `10`, `101` as   `10APT`) — use the display number when talking to riders, and match on it against   `announcement.php`\'s `line_number`. * `all_stations` is every leg of the line **concatenated** (outbound, branch   variants and the return trip) — it is not a single one-way path. Return legs mostly   use their own stop IDs, so the list does not repeat IDs at the turnaround. * A few stop IDs in `all_stations` are not present in `Network.stations`; skip them. * `line_type_color_active` was `#000000` for every line when checked, so it carries   no usable line color. 

## Properties

Name | Type
------------ | -------------
`id` | string
`lineNumber` | string
`lineNumberForDisplay` | string
`actualLineNumber` | string
`lineTitle` | string
`lineTitleForDisplay` | string
`directionIdForDisplay` | string
`priceVariationId` | string
`lineType` | string
`lineTypeColorActive` | string
`lineTypeColorInactive` | string
`allStations` | Array&lt;string&gt;

## Example

```typescript
import type { Line } from ''

// TODO: Update the object below with actual values
const example = {
  "id": 21432,
  "lineNumber": 10,
  "lineNumberForDisplay": 1,
  "actualLineNumber": 10,
  "lineTitle": KLISA - CENTAR - LIMAN 1,
  "lineTitleForDisplay": null,
  "directionIdForDisplay": null,
  "priceVariationId": null,
  "lineType": 1,
  "lineTypeColorActive": #000000,
  "lineTypeColorInactive": #000000,
  "allStations": null,
} satisfies Line

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Line
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


