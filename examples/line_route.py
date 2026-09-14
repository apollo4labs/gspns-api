#!/usr/bin/env python3
"""Tutorial 3 — Dump a bus line's full route as GeoJSON.

Run:  python3 line_route.py 7A 6532
Then drag the output file into https://geojson.io to see the route on a map.
"""
import json
import sys
import urllib.request

API_KEY = "4670f468049bbee2260"
BASE = "https://online.nsmart.rs"


def fetch(url):
    req = urllib.request.Request(url, headers={"X-Api-Authentication": API_KEY})
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
    line = sys.argv[1] if len(sys.argv) > 1 else "7A"
    station = int(sys.argv[2]) if len(sys.argv) > 2 else 6532
    route = get_line_route(line, station)
    out = f"line_{line}.geojson"
    with open(out, "w") as f:
        json.dump(route, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(route['geometry']['coordinates'])} stops → {out}")