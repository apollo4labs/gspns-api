<div align="center">

# 🚌 GSPNS API — Novi Sad Public Transport

**Unofficial, reverse-engineered documentation of the GSPNS (JGSP "Novi Sad") public transport API**

The same backend that powers the **NSmart** mobile app — now documented as a clean
OpenAPI 3.0.3 spec with live examples, sample responses and a full tutorial.

[![OpenAPI 3.0.3](https://img.shields.io/badge/OpenAPI-3.0.3-6BA81E)](openapi.yaml)
[![JSON](https://img.shields.io/badge/format-JSON-blue)](openapi.yaml)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/apollo4labs/gspns-api/pulls)

*Built for a university course · Not affiliated with GSPNS or BusLogic/NSmart*

</div>

---

## ✨ What is this?

JGSP "Novi Sad" (GSPNS) runs the public bus network of **Novi Sad, Serbia** (60+ lines,
450+ stations). Its digital services — the NSmart app, ticket machines, station displays —
talk to a JSON API at **`online.nsmart.rs`**. That API has no public documentation, so we
reverse-engineered it:

* 🔍 recovered the endpoints, auth model and API key from the public Android APK
* 🧪 verified every endpoint against the live API
* 📜 consolidated everything into `openapi.yaml` — a valid **OpenAPI 3.0.3** spec
* 🖥️ included a **Swagger UI** page so you can browse and test the API in your browser
* 📚 wrote a **step-by-step tutorial** (`TUTORIAL.md`) with real examples

> **What you can do with it:** query the full network (cities → stations → routes),
> get **live bus positions and arrival ETAs** for any station, and inspect the ticketing
> backend — all from a simple `curl` call.

---

## 📁 Repository layout

| Path | What it is |
|---|---|
| [`openapi.yaml`](openapi.yaml) | ⭐ The OpenAPI 3.0.3 specification (the main deliverable) |
| [`index.html`](index.html) | Swagger UI page — browse & try the API in a browser |
| [`TUTORIAL.md`](TUTORIAL.md) | 📚 Step-by-step usage tutorial with code examples |
| [`docs/data-notes.md`](docs/data-notes.md) | Payload details for building a real client: line numbers, stop lists, placeholders |
| [`docs/timetables.md`](docs/timetables.md) | Scheduled departures — the official gspns.co.rs pages (not part of this API) |
| [`examples/`](examples) | Ready-to-run scripts (Python, Node.js) |
| [`samples/`](samples) | Raw responses captured from the live API |
| [`index.html`](index.html) | Swagger UI page (loads assets from CDN with local fallback) |

---

## 🚀 Quick start

### 1. Browse the docs (2 ways)

**Option A — local Swagger UI (recommended):**

```bash
git clone https://github.com/apollo4labs/gspns-api.git
cd gspns-api
python3 -m http.server 8080
# open http://localhost:8080
```

The page loads Swagger UI from a CDN automatically (with local fallback), so you only
need an internet connection for the UI itself — `openapi.yaml` is fully local.

**Option B — no installation:** paste `openapi.yaml` into
[editor.swagger.io](https://editor.swagger.io) — instant interactive docs.

### 2. Make your first call

```bash
# Live arrivals at station 6532 ("Narodnog fronta-Šekspirova"), all lines
curl 'https://online.nsmart.rs/publicapi/v1/announcement/announcement.php?ibfm=TM00000&station_uid=6532' \
  -H 'X-Api-Authentication: 4670f468049bbee2260'
```

That's it — you'll get real-time buses with GPS positions and ETAs. 🎉

---

## 🔑 Authentication

Every request needs one header:

```
X-Api-Authentication: 4670f468049bbee2260
```

The key is **static and identical for every install** — it's compiled into the public
NSmart APK (`res/values/strings.xml` → `company_api_key`). Treat it as public knowledge,
not a secret. All endpoints in this repo include it in their OpenAPI `security` block.

---

## 🧭 Endpoints at a glance

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/publicapi/v1/networkextended.php` | Full static network: cities, stations, line pairs |
| `GET` | `/publicapi/v1/announcement/announcement.php` | ⭐ **Live arrivals & vehicle GPS** per station |
| `POST` | `/publicapi/v1/rest_options/android_login.php` | Account actions (login, register, …) |
| `POST` | `/publicapi/v1/rest_options/android_additional_options.php` | Card / ticket options |
| `POST` | `/publicapi/v1/rest_options/android_additional_settings.php` | User settings |
| `POST` | `/publicapi/v1/rest_options/android_allsecure.php` | Payment gateway (AllSecure) |
| `POST` | `/publicapi/v1/rest_options/android_add_or_connect_card.php` | Connect a physical card |
| `POST` | `/publicapi/v1/rest_options/android_prepaid_cards_log_online.php` | Prepaid card logs |
| `POST` | `/api/api.php` | Legacy generic dispatcher |

The two that matter for transport data are **`networkextended.php`** (static) and
**`announcement.php`** (realtime).

---

## 💡 Core concepts

* **City** — a municipality in the network. **Novi Sad = id `72`**, 452 stations.
* **Station** — a bus stop with a numeric `station_uid` (e.g. `6532`).
* **Pair** — a line-pair ID used for route reconstruction (one per station per direction).
* **`ibfm`** — the line filter: `TM00000` = all lines, `7A` = only line 7A.
* **Announcement** — one approaching vehicle: ETA in seconds, GPS position, route title,
  full station sequence with coordinates.

---

## 🧪 Example calls

### Live arrivals at a station

```bash
curl -s 'https://online.nsmart.rs/publicapi/v1/announcement/announcement.php?ibfm=TM00000&station_uid=6532' \
  -H 'X-Api-Authentication: 4670f468049bbee2260'
```

```json
[{
  "seconds_left": 1670,
  "line_number": "7A",
  "station_name": "Narodnog fronta-Šekspirova",
  "stations_between": 17,
  "garage_no": "1102",
  "line_title": "NOVO NASELJE - ŽELEZNIČKA STANICA - FUTOŠKA PIJACA - LIMAN 4 - NOVO NASELJE",
  "vehicles": [{"garageNo": "1102", "lat": "45.24890660", "lng": "19.79147330"}],
  "all_stations": [{"id": 13219, "coordinates": {"latitude": "45.2481177952", "longitude": "19.7860623227"}}]
}]
```

### Full network (cities & stations)

```bash
curl -s -X POST 'https://online.nsmart.rs/publicapi/v1/networkextended.php' \
  -H 'X-Api-Authentication: 4670f468049bbee2260' \
  -H 'Content-Type: application/json' \
  -d '{"action":"get_cities_extended"}'
```

### Filter by a single line

```bash
curl -s 'https://online.nsmart.rs/publicapi/v1/announcement/announcement.php?ibfm=7A&station_uid=6532' \
  -H 'X-Api-Authentication: 4670f468049bbee2260'
```

More examples (Python, Node.js, JavaScript fetch) in the [tutorial](TUTORIAL.md) and
[`examples/`](examples).

---

## ⚠️ Known quirks (read before coding against it)

1. **The big network payload is fragile.** `networkextended.php` returns ~1.2 MB and the
   server frequently **corrupts/truncates the stream** mid-body (raw control characters,
   null-byte runs, dropped chunks). Always re-request on JSON parse failure — the official
   app does exactly that.
2. **`action` values are loose.** `get_cities_extended`, `get_network`, `get_trips` and
   `get_schedule` all return the same cities payload.
3. **Unknown station IDs** return `[{"success":false,"code":3}]` — not a 404.
4. **Coordinates arrive as strings** (`"45.24890660"`) in announcements, but as numbers in
   the network payload. Cast defensively (`parseFloat` / `float()`).
5. **Missing `action`** on the `rest_options/*` dispatchers returns a plain-text Serbian
   error (`POTREBAN JE PARAMETAR ACTION`), not JSON.
6. **Registration is disabled** for JGSP Novi Sad: `action=register` →
   `{"success":false,"msg":"SIGNUP_FORM_NOT_CONFIGURED"}`.
7. **"Nothing due" is a placeholder, not `[]`.** A known station with no approaching bus
   returns `[{"just_coordinates":"1", ...}]`; keep only entries with a numeric `seconds_left`.
8. **GPS `0,0` means unknown.** Vehicles without a fix are reported at latitude/longitude
   `"0.00000000"`.
9. **`networkextended.php` has more than `cities`** — flat `stations` and `lines` lists, where
   a line's `all_stations` is every leg concatenated. See [`docs/data-notes.md`](docs/data-notes.md).
10. **No timetables here.** Scheduled departures live on gspns.co.rs — see
    [`docs/timetables.md`](docs/timetables.md).

---

## 🔬 How it was reverse-engineered

1. **Find the app** — GSPNS's digital services run on **NSmart** (`buslogic.nsmartapp`).
2. **Extract endpoints & key** — `strings` over `classes*.dex` / `resources.arsc` revealed
   the REST paths; decompiling `SplashActivity` led to `company_api_key` in `strings.xml`.
3. **Probe the live API** — every discovered path was hit with the key; request formats and
   response schemas were mapped from real responses (see [`samples/`](samples)).
4. **Consolidate into OpenAPI 3.0.3** — validated with `swagger-cli` / `@redocly/cli`.

Credit: the APK-level groundwork was documented by the
[FmasterofU/NSmart-RE](https://github.com/FmasterofU/NSmart-RE) community project.

---

## 📖 Tutorial

The full beginner-to-intermediate tutorial is in **[`TUTORIAL.md`](TUTORIAL.md)** —
covers curl, Python and Node.js, the data model, error handling and a mini project idea.

---

## 🛡️ Ethics & fair use

* This is **unofficial** documentation for **educational purposes**. GSPNS publishes no
  third-party API policy, so please be a good citizen: low request rates, no bulk scraping,
  nothing beyond what a single user needs.
* The API key ships with the public app; nothing here bypasses security.
* **Do not use the account/wallet/payment endpoints** except for study — they touch real
  payment infrastructure.

---

## 📜 License

MIT — see [LICENSE](LICENSE). The API itself belongs to its operators, not us.

---

<div align="center">

⭐ **If this helped your project, star the repo!** · Issues & PRs welcome

*Made with ☕ and a lot of `curl` for a university course*

</div>