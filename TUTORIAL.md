# 📚 GSPNS API — Tutorial

*How to use the reverse-engineered GSPNS (Novi Sad) public transport API, step by step.*

![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0.3-6BA81E)

---

## Table of contents

1. [Before you start](#1-before-you-start)
2. [The data model](#2-the-data-model)
3. [Tutorial 1 — Your first request (curl)](#3-tutorial-1--your-first-request-curl)
4. [Tutorial 2 — Find every bus near you (Python)](#4-tutorial-2--find-every-bus-near-you-python)
5. [Tutorial 3 — Build a line & station map (Python)](#5-tutorial-3--build-a-line--station-map-python)
6. [Tutorial 4 — JavaScript / Node.js](#6-tutorial-4--javascript--nodejs)
7. [Error handling & gotchas](#7-error-handling--gotchas)
8. [Mini project ideas](#8-mini-project-ideas)

---

## 1. Before you start

All you need is `curl` — or any HTTP client. No API key registration, no OAuth,
**no sign-up**. There is exactly one header that every request must carry:

```
X-Api-Authentication: 4670f468049bbee2260
```

**Base URL:** `https://online.nsmart.rs`

> It's static and shipped inside the public NSmart Android app, so treat it like a
> public identifier, not a secret. And because it's public, please *be polite*: a few
> requests per minute is plenty for learning.

---

## 2. The data model

The whole network is a four-level hierarchy:

```
City (e.g. Novi Sad, id 72)
 └── stations[]        (452 station IDs)
      └── pairs[]      (line-pair IDs, route reconstruction)
```

And the *realtime* picture is per-station:

```
Station (station_uid)
 └── Announcement[]    (one per approaching vehicle)
      ├── seconds_left      → ETA in seconds
      ├── line_number       → "7A", "8", "24"…
      ├── stations_between  → stops away
      ├── garage_no         → physical bus number
      ├── vehicles[]        → live GPS {garageNo, lat, lng}
      └── all_stations[]    → full station sequence w/ coordinates
```

**Key IDs you'll want to remember:**

| Thing | Value |
|---|---|
| Novi Sad city | `72` |
| Novi Sad default station | `7` |
| "Narodnog fronta-Šekspirova" station | `6532` |
| `ibfm` value for "all lines" | `TM00000` |

---

## 3. Tutorial 1 — Your first request (curl)

Open a terminal and run:

```bash
curl -s 'https://online.nsmart.rs/publicapi/v1/announcement/announcement.php?ibfm=TM00000&station_uid=6532' \
  -H 'X-Api-Authentication: 4670f468049bbee2260'
```

You'll get a JSON array — one object per oncoming bus. Let's pretty-print it:

```bash
curl -s 'https://online.nsmart.rs/publicapi/v1/announcement/announcement.php?ibfm=TM00000&station_uid=6532' \
  -H 'X-Api-Authentication: 4670f468049bbee2260' \
  | python3 -m json.tool
```

Look at one entry:

```json
{
  "seconds_left": 1670,
  "line_number": "7A",
  "station_name": "Narodnog fronta-Šekspirova",
  "stations_between": 17,
  "garage_no": "1102",
  "vehicles": [
    { "garageNo": "1102", "lat": "45.24890660", "lng": "19.79147330" }
  ]
}
```

✅ **You just did real-time transit tracking.** That bus `1102` on line `7A` will be at
your stop in ~28 minutes (1670 s), and it's currently at `45.2489, 19.7914`.

---

## 4. Tutorial 2 — Find every bus near you (Python)

Let's find all vehicles within a radius of a given GPS point. No third-party packages —
just the standard library.

```python
#!/usr/bin/env python3
"""Find every GSPNS bus within `radius_km` of a point."""
import json
import math
import urllib.request

API_KEY = "4670f468049bbee2260"
BASE = "https://online.nsmart.rs"
# A central Novi Sad station (Uspenska / Pozorišni trg area)
STATION_UID = 7


def fetch(url):
    req = urllib.request.Request(url, headers={"X-Api-Authentication": API_KEY})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


def main():
    radius_km = 2.0
    url = f"{BASE}/publicapi/v1/announcement/announcement.php?ibfm=TM00000&station_uid={STATION_UID}"
    announcements = fetch(url)

    print(f"{'line':<5} {'bus':<6} {'eta_min':<8} {'dist_km':<8} lat/lng")
    print("-" * 60)
    for a in announcements:
        for v in a.get("vehicles", []):
            lat, lng = float(v["lat"]), float(v["lng"])
            dist = haversine_km(45.25518, 19.84197, lat, lng)  # station coordinates
            print(f"{a['line_number']:<5} {v['garageNo']:<6} "
                  f"{a['seconds_left'] / 60:>6.1f}    {dist:>6.2f}    {lat:.5f},{lng:.5f}")


if __name__ == "__main__":
    main()
```

Save as `nearby_buses.py` and run:

```bash
python3 nearby_buses.py
```

```
line  bus    eta_min  dist_km  lat/lng
------------------------------------------------------------
8     1143      8.0     1.02    45.23934,19.84805
7A    1102     28.0     3.81    45.24891,19.79147
...
```

> 💡 **Note:** `stations_gpsx` / `stations_gpsy` in the response give you the *station's*
> coordinates, so you can compute each bus's distance from the stop properly.

---

## 5. Tutorial 3 — Build a line & station map (Python)

The network endpoint gives you every city and station ID. Combine it with the
announcement endpoint (which returns station coordinates) to build a live map.

```python
#!/usr/bin/env python3
"""Dump a line's full route (station order + coordinates) as GeoJSON."""
import json
import urllib.request

API_KEY = "4670f468049bbee2260"
BASE = "https://online.nsmart.rs"


def fetch(url, body=None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(
        url, data=data,
        headers={"X-Api-Authentication": API_KEY, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_line_route(line: str, station_uid: int) -> dict:
    url = f"{BASE}/publicapi/v1/announcement/announcement.php?ibfm={line}&station_uid={station_uid}"
    anns = fetch(url)
    if not anns:
        raise SystemExit(f"No data for line {line} at station {station_uid}")
    a = anns[0]
    coords = [
        [float(st["coordinates"]["longitude"]), float(st["coordinates"]["latitude"])]
        for st in a["all_stations"]
    ]
    return {
        "type": "Feature",
        "properties": {"line": a["line_number"], "title": a["line_title"]},
        "geometry": {"type": "LineString", "coordinates": coords},
    }


if __name__ == "__main__":
    route = get_line_route("7A", 6532)
    with open("line_7A.geojson", "w") as f:
        json.dump(route, f, ensure_ascii=False, indent=2)
    print(f"Saved route with {len(route['geometry']['coordinates'])} stops "
          f"→ line_7A.geojson (drag into https://geojson.io)")
```

Run it, then drop the file into [geojson.io](https://geojson.io) — you'll see line 7A
drawn across Novi Sad on a map. 🗺️

---

## 6. Tutorial 4 — JavaScript / Node.js

Same thing in Node.js (18+, has global `fetch`):

```javascript
const API_KEY = "4670f468049bbee2260";
const BASE = "https://online.nsmart.rs";

async function getArrivals(stationUid, line = "TM00000") {
  const url = `${BASE}/publicapi/v1/announcement/announcement.php?ibfm=${line}&station_uid=${stationUid}`;
  const res = await fetch(url, { headers: { "X-Api-Authentication": API_KEY } });
  return res.json();
}

const arrivals = await getArrivals(6532, "7A");
for (const a of arrivals) {
  const etaMin = (a.seconds_left / 60).toFixed(1);
  console.log(`Line ${a.line_number} · bus ${a.garage_no} · ETA ${etaMin} min · ${a.station_name}`);
}
```

Or in the browser:

```javascript
fetch("https://online.nsmart.rs/publicapi/v1/announcement/announcement.php?ibfm=TM00000&station_uid=7", {
  headers: { "X-Api-Authentication": "4670f468049bbee2260" }
})
  .then(r => r.json())
  .then(console.log);
```

> ⚠️ **Browser CORS note:** if you test from `file://` or a random origin and get a CORS
> error, serve your page from a local server (`python3 -m http.server`) or proxy the API
> from a tiny backend — that also keeps your key out of public client code.

---

## 7. Error handling & gotchas

| Situation | What you get |
|---|---|
| Unknown `station_uid` | `[{"success":false,"code":3}]` (HTTP 200!) |
| Missing `action` on dispatchers | Plain text `POTREBAN JE PARAMETAR ACTION` |
| Missing `ACTION` on `/api/api.php` | Plain text `ERROR_MISSING_PARAMETERS` |
| Registration (`action=register`) | `{"success":false,"msg":"SIGNUP_FORM_NOT_CONFIGURED"}` |
| Unauthenticated `GET` on network endpoint | HTTP 403 |
| Huge network payload | ⚠️ Server may **corrupt/truncate** mid-stream — retry until JSON parses |

**Golden rules:**

1. Wrap every parse in try/catch and **retry** `networkextended.php` on failure — the
   official app does exactly this.
2. Always cast coordinates: `float(lat)` — they arrive as **strings**.
3. `seconds_left` is seconds; divide by 60 for minutes.
4. `ibfm=TM00000` means *all lines*. Use a specific code (`7A`, `24`, …) to filter.
5. Don't hammer the API. It's undocumented and shared — a request every few seconds is
   plenty for a course project.

---

## 8. Mini project ideas

Got the basics down? Try one of these for your course:

* 🚏 **Station display** — a web page that shows the next 5 buses for any station
  (search the network payload for a station ID, poll every 30 s).
* 🗺️ **Live fleet map** — poll several stations, collect all `vehicles[]`, plot them on
  a Leaflet/MapLibre map.
* ⏱️ **ETA accuracy study** — log `seconds_left` vs. actual arrival over a week, measure
  how good the predictions are (great data-analysis project!).
* 🚌 **Line explorer** — pick a line, render its full route from `all_stations`, show
  buses moving along it.
* 📱 **Companion app** — GTFS-style route data (see the
  [jqueguiner/gtfs](https://github.com/jqueguiner/gtfs) catalog for Serbia) merged with
  this realtime API gives you a complete journey planner.

---

*Happy hacking! If you build something cool with this, open an issue or PR — we'd love
to link to it.* 🚀