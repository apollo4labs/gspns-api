# GSPNS / NSmart Public Transport API — Reverse Engineering (Novi Sad)

Unofficial, reverse-engineered documentation of the API behind the **GSPNS**
(JGSP "Novi Sad") public transport network — the same backend powering the
**NSmart** mobile app (`buslogic.nsmartapp`).

**What's in this repo:**

| File | Purpose |
|---|---|
| `openapi.yaml` | OpenAPI 3.0.3 specification of the API |
| `index.html` | Self-contained Swagger UI page (renders `openapi.yaml`) |
| `swagger-ui/` | Local Swagger UI assets (works offline) |
| `samples/` | Raw responses captured from the live API |
| `README.md` | This document — methodology + findings |

---

## Quick start

Serve this directory with any static file server and open `index.html`:

```bash
cd gspns-api
python3 -m http.server 8080
# → http://localhost:8080
```

No build step, no dependencies. Swagger UI assets are vendored locally so the
site works fully offline (handy for a university presentation).

---

## The API in one paragraph

* **Base URL:** `https://online.nsmart.rs`
* **Auth:** header `X-Api-Authentication: 4670f468049bbee2260`
  (static key compiled into the public Android APK — same for every install)
* **Transport:** HTTPS, JSON responses, UTF-8 (Serbian diacritics)
* **Two public endpoint families:**
  1. **Network** — `POST /publicapi/v1/networkextended.php` → all cities,
     station lists and line pairs (Novi Sad = city `72`, 452 stations).
  2. **Realtime** — `GET /publicapi/v1/announcement/announcement.php`
     → per-station live arrivals: seconds left, vehicle GPS, line route,
     up to the full station sequence with coordinates.
  3. **Account / wallet / payments** — `POST /publicapi/v1/rest_options/*.php`
     dispatchers (login, cards, e-wallet, AllSecure payments…).

---

## Minimal examples

### 1. Static network (cities & stations)

```bash
curl -s -X POST 'https://online.nsmart.rs/publicapi/v1/networkextended.php' \
  -H 'X-Api-Authentication: 4670f468049bbee2260' \
  -H 'Content-Type: application/json' \
  -d '{"action":"get_cities_extended"}'
```

**Novi Sad** entry: `{"id":72,"name":"Novi Sad","default_station":7,"stations":[...452 ids...]}`
Station details are not embedded — the app fetches them per station via the
announcement endpoint (below).

### 2. Live arrivals at a station

```bash
# station 6532 = "Narodnog fronta – Šekspirova", all lines
curl -s 'https://online.nsmart.rs/publicapi/v1/announcement/announcement.php?ibfm=TM00000&station_uid=6532' \
  -H 'X-Api-Authentication: 4670f468049bbee2260'

# only line 7A at the same station
curl -s 'https://online.nsmart.rs/publicapi/v1/announcement/announcement.php?ibfm=7A&station_uid=6532' \
  -H 'X-Api-Authentication: 4670f468049bbee2260'
```

Response (one object per approaching vehicle):

```json
[{
  "seconds_left": 1670,
  "line_number": "7A",
  "station_name": "Narodnog fronta-Šekspirova",
  "actual_line_number": "7A",
  "stations_between": 17,
  "garage_no": "1102",
  "line_title": "NOVO NASELJE - ŽELEZNIČKA STANICA - FUTOŠKA PIJACA - LIMAN 4 - NOVO NASELJE",
  "vehicles": [{"garageNo": "1102", "lat": "45.24890660", "lng": "19.79147330"}],
  "all_stations": [{"id": 13219, "coordinates": {"latitude": "45.2481177952", "longitude": "19.7860623227"}}, "..."]
}]
```

### 3. Account dispatch (for completeness)

```bash
curl -s -X POST 'https://online.nsmart.rs/publicapi/v1/rest_options/android_login.php' \
  -H 'X-Api-Authentication: 4670f468049bbee2260' \
  -d 'action=register'
# → {"success":false,"msg":"SIGNUP_FORM_NOT_CONFIGURED"}  (registration disabled for JGSP NS)
```

---

## Reverse-engineering methodology

1. **Find the app.** GSPNS's digital ticketing/passenger-info app is
   **NSmart** (`buslogic.nsmartapp`, Google Play). The companion
   repo [FmasterofU/NSmart-RE](https://github.com/FmasterofU/NSmart-RE)
   documents APK-level RE with `strings`, `dex2jar` and `jd-gui`.

2. **Extract the endpoints.** Running `strings` over `classes*.dex` /
   `resources.arsc` reveals the REST paths:
   ```
   /publicapi/v1/networkextended.php
   /publicapi/v1/announcement/announcement.php
   /publicapi/v1/rest_options/android_login.php
   /publicapi/v1/rest_options/android_add_or_connect_card.php
   /publicapi/v1/rest_options/android_additional_options.php
   /publicapi/v1/rest_options/android_additional_settings.php
   /publicapi/v1/rest_options/android_allsecure.php
   /publicapi/v1/rest_options/android_prepaid_cards_log_online.php
   /api/api.php
   ```
   plus ~40 Java API classes (`CitiesExtendedApi`, `AnnouncementApi`,
   `SearchedStationChosenApi`, `EWalletStatusApi`, `OnlineQrCodeGeneratorApi` …).

3. **Extract the API key.** Decompile → `SplashActivity` reads
   `company_api_key` from resources → `res/values/strings.xml`:
   `<string name="company_api_key">4670f468049bbee2260</string>`.
   It is a **static, non-secret** key shipped with the app.

4. **Probe the live API (this project).** With the key in hand we hit
   every discovered path and mapped request formats and response schemas
   (see `openapi.yaml`). Notable live-API quirks:

   * The full network dump is ~1.2 MB and the server **corrupts/truncates
     the stream** under normal download speeds (raw control chars, null-byte
     runs, dropped chunks). The response is not always valid JSON — the app
     tolerates it, and so should your parser. Retry until parseable.
   * `networkextended.php` accepts several `action` values
     (`get_cities_extended`, `get_network`, `get_trips`, `get_schedule`)
     and returns the **same** cities payload for all of them.
   * `announcement.php` returns `[{"success":false,"code":3}]` for unknown
     station IDs.
   * `ibfm=TM00000` = "all lines"; `ibfm=7A` filters a single line.
   * Missing `action` on dispatchers → plain-text Serbian error
     (`POTREBEN JE PARAMETAR ACTION` / `ERROR_MISSING_PARAMETERS`),
     not JSON.
   * Coordinates arrive as **strings** (e.g. `"45.24890660"`) in the
     announcement payload and as numbers in the network payload.

5. **Consolidate into OpenAPI 3.0.3.** Every endpoint observed — plus
   documented-but-unverified flows from the APK class inventory (e-wallet,
   AllSecure payments, monthly cards, QR tickets) — is captured in
   `openapi.yaml`, validated with `swagger-cli` (now `@redocly/cli`).

---

## Reliability / ethics note

* This is **unofficial** documentation. GSPNS has no public API policy for
  third parties; this project is for **educational purposes** (university
  course). Use it politely — low request rates, no scraping beyond what a single
  user doing the same queries needs.
* The API key is public knowledge (shipped in the app). Nothing here
  bypasses authentication — we document what the app itself does.
* Do **not** use the account/wallet endpoints except for study — they touch
  real payment infrastructure.

---

## Files captured from the live API (`samples/`)

* `sample-announcement.json` — all lines at station 6532 (5 vehicles)
* `sample-announcement-line7A.json` — line 7A filtered at station 6532
* `novi-sad-city.json` — Novi Sad city entry (id 72, 452 stations)
* `sample-cities-extended.json` — raw (corrupted) network dump, kept as
  evidence of the truncation quirk
* `cities-try1.json` / `cities-try2.json` — retry attempts showing
  different truncation points

---

## Useful references

* <https://github.com/FmasterofU/NSmart-RE> — APK reverse engineering walkthrough
* <https://github.com/jqueguiner/gtfs> — public-transport catalog (GTFS feeds,
  incl. Serbia) if you want a GTFS view of the network
* <https://online.nsmart.rs> — NSmart web portal (JGSP Novi Sad)