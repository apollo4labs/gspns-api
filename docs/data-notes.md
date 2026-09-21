# Data notes: working with the network and live payloads

Things learned while building a real client (a trip planner and live station map for Novi Sad)
on top of `networkextended.php` and `announcement.php`. Everything here was checked against
the live API in September 2026; counts are a snapshot and will drift.

## `networkextended.php` at a glance

A `GET` with the API key and no parameters returns the payload (~1.5 MB), as does the `POST`
documented in `openapi.yaml`. Top-level keys:

| Key | Contents |
|---|---|
| `cities` | 43 cities (Novi Sad is `72`) |
| `stations` | 1013 stations across all cities — 406 in Novi Sad, plus Futog, Sremska Kamenica, Petrovaradin, Veternik, … |
| `lines` | 104 lines — 73 direction `A`, 31 direction `B` |
| `bike_sharing` | `{"pylons": []}` (empty) |
| `smart_parking` | `{"parking_sensors": []}` (empty) |

`stations` and `lines` are the useful parts; `cities` only lists station IDs.

## Lines

* **Display number vs internal code.** `line_number_for_display` is the number riders know and
  is unique across the 104 entries. `line_number` / `actual_line_number` are internal and
  can differ: internal `10` → displayed `1`, `41` → `10`, `101` → `10APT`, `110` → `11A`,
  `120B` → `12`. `announcement.php` reports the display number in `line_number`, so match on
  that.
* **`all_stations` is all legs concatenated.** It contains the outbound trip, branch
  variants and the return trip back to back, and it is not a clean one-way path. The
  return direction mostly uses its own separate stop IDs, so IDs don't repeat at the
  turnaround. To get one direction, cut the list at the turnaround (for example the stop
  farthest from the first one).
* **Unknown stop IDs.** A few entries in `all_stations` (33 of 5613 in the snapshot) have no
  matching station in `stations`; skip them.
* **No geometry.** The API has stop sequences but no polylines. Connecting the stops with
  straight lines is the best you can do from this API alone; snap to roads with a routing
  engine if you need a realistic path.
* **No usable colors.** `line_type_color_active` is `#000000` for all 104 lines. Line colors
  have to come from another source (the operator's line-network map on gspns.co.rs shows
  them).
* **`line_type`** is `1` (37 lines), `2` (49) or `3` (18).

## Stations

* `id` (integer) is the value for `announcement.php`'s `station_uid` and appears (as a
  string) in `Line.all_stations`. `station_id` is a different, operator-internal code.
* `lines_for_station` / `lines_for_station_additional_data` list the lines stopping at the
  station by display number, which makes "which lines serve this stop" a single lookup
  instead of a scan over every line.
* Coordinates are **strings** here (`"45.3141430070"`), while `cities[].coordinates` are numbers.

## Live arrivals (`announcement.php`)

* **Nothing due ≠ empty array.** A known station with no approaching bus returns one
  placeholder object, e.g. `{"gpsx": "...", "gpsy": "...", "just_coordinates": "1",
  "station_name": "Agrovojvodina", "station_uid": 6801}`. Unknown stations return
  `[{"success": false, "code": 3}]`. Keep only entries with a numeric `seconds_left` and an
  array `vehicles`.
* **Position `0,0` means "unknown".** A vehicle without a GPS fix is reported at
  `lat "0.00000000"`, `lng "0.00000000"`, often with an empty `garageNo`. Drop those before
  drawing a marker or measuring distances.
* **`stations_between` counts the stops the vehicle still has to call at before this
  station**, so `0` means this station is its very next stop and "stops away" is
  `stations_between + 1`. If the station is at index `t` in `all_stations`, the vehicle is
  heading for index `t - stations_between`; in live samples the bus sat at or just before that
  stop.
* **Loop lines list a station twice** in `all_stations`. `stations_between` resolves which
  pass the vehicle is on: among the occurrences that leave room for that many stops before
  them, take the one whose `t - stations_between` stop is nearest the vehicle. Without it you
  have to guess from geometry.
* `all_stations` here is the whole line, not just the stops the vehicle still has to visit.
* Coordinates are strings, as above.

## Caching

The network payload changes rarely, so fetching it once per hour is plenty; `announcement.php`
is the only realtime call, and results for one station are fine to reuse for ~20 seconds. The
API sends no CORS headers, so browser apps need a same-origin proxy or edge function that adds
the `X-Api-Authentication` header.

## Scheduled timetables

Not available from this API — see [`timetables.md`](timetables.md).
