# Scheduled timetables (gspns.co.rs)

The NSmart API in `openapi.yaml` only knows **live** arrivals. It has no scheduled
departure times. Those are published on the operator's own website,
`www.gspns.co.rs/red-voznje` ("red vožnje" = timetable), as HTML fragments that the page
loads with AJAX. This note documents those fragments so they can be read programmatically.

These pages are **not** part of the NSmart API: no API key is needed, and the response is HTML,
not JSON. They were checked against the live site in September 2026.

> **Plain HTTP only.** The site's TLS certificate does not validate, so `https://` requests
> fail (curl exits with a certificate error). Use `http://www.gspns.co.rs/...`.

Send `X-Requested-With: XMLHttpRequest` like the site's own scripts do. Please keep the
request rate low — a full crawl is several hundred small requests, so do it at most monthly
and with a small concurrency limit.

## Parameters

| Parameter | Values | Meaning |
|---|---|---|
| `rv` | `rvg` / `rvp` | Network: `rvg` = city (*gradski*), `rvp` = suburban (*prigradski*) |
| `vaziod` | `YYYY-MM-DD` | "Valid from" date of a timetable version |
| `dan` | `R` / `S` / `N` / `P` | Day type: workday, Saturday, Sunday, holiday |
| `linija[]` | e.g. `2.`, `1*` | Line value taken from `lista-linija` (see below) |

## Endpoints

All paths are relative to `http://www.gspns.co.rs/red-voznje/`.

### `GET gradski` — the timetable page

Returns the full page. The `<select name=vaziod>` on it lists every timetable version that
can be requested (`<option value="2026-09-01">`). Read this list rather than hard-coding a
date: a checked-in date goes stale as soon as a new timetable version is published.

### `GET lista-linija?rv=…&vaziod=…&dan=…` — lines with a timetable

Returns `<option>` elements, one per line that has a timetable for that network, version and
day type:

```html
<option value="1*">1 KLISA-CENTAR-LIMAN I</option>
<option value="2.">2 CENTAR - NOVO NASELJE</option>
<option value="3A.">3A ZEL.STANICA ...</option>
```

The `value` is what `ispis-polazaka` expects in `linija[]`. It carries a trailing marker
(`.` or `*`) that is not part of the line number: strip it (`[.*]+$`) to get the number
riders know.  The list is per day type, so ask for each `dan` separately.

### `GET ispis-polazaka?rv=…&vaziod=…&dan=…&linija[]=…` — departures of one line

Returns the departure table for one line, both directions side by side:

```html
<div class=table-title> Линија : 2 CENTAR - NOVO NASELJE </div>
<table class="table table-bordered tabela-polasci">
  <tr>
    <th>Смер A: CENTAR - NOVO NASELJE </th>
    <th>Смер B: NOVO NASELJE - CENTAR </th>
  </tr>
  <tr>
    <td valign='top' width='50%'>            <!-- direction A -->
      <br/><b>05</b>
        <sup><font size=-1><span class='niskopodni-rampa '>00<b></b></span></font></sup>
        <sup><font size=-1><span class=' '>57<b></b></span></font></sup>
      <br/><b>06</b> ...
```

How to read it:

* One `<th>` and one `<td valign='top' width='50%'>` per direction. A one-direction line has a
  single of each; the cells are in the same order as the headers (**A**, then **B**).
* Inside a cell, `<b>HH</b>` starts an hour and each `<span>MM<b>…</b></span>` is one
  departure in that hour. Late-night departures can be printed as hours `24`, `25`, …;
  take them modulo 24 for a time of day.
* A `<span>` whose class contains `niskopodni` (e.g. `niskopodni-rampa`) marks a
  **low-floor** vehicle — the site renders it as a green underline.
* The `<b>` inside the span holds a variant marker explained in the legend; it is empty
  for regular departures.
* The footer cell (`tabelapolascifooter`) holds the legend text for those markers. It ends
  with a fixed "green underline = low-floor" sentence that duplicates the class above.
* Text is Serbian Cyrillic in the headers and Latin in the line names; entities such as
  `&quot;` and `&amp;` appear in names.

## Suggested crawl

1. `GET gradski` → list the `vaziod` dates.
2. For each date × network (`rvg`, `rvp`) × day type (`R`, `S`, `N`, `P`):
   `GET lista-linija` → the lines that run.
3. For each line: `GET ispis-polazaka` and parse the table.
4. Re-run monthly — timetables change rarely (new versions come with a new `vaziod` date).

Store the version (`vaziod`) with each departure so a newly published timetable does not
overwrite the one still in force.

## Joining with the live API

The timetable uses the rider-facing **line number** (`2`, `7A`), which matches
`Line.line_number_for_display` from `networkextended.php` and `line_number` from
`announcement.php`. The timetable is per line and direction, not per station, so a station's
scheduled times are the line's first-stop times shifted by travel time — the schedule pages do not
give per-stop times.
