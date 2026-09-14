#!/usr/bin/env python3
"""Tutorial 2 — Find every GSPNS bus near a station, with ETA and distance.

Pure standard library. Run:  python3 nearby_buses.py
"""
import json
import math
import urllib.request

API_KEY = "4670f468049bbee2260"
BASE = "https://online.nsmart.rs"
# Central Novi Sad station: Uspenska / Pozorišni trg
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
    url = f"{BASE}/publicapi/v1/announcement/announcement.php?ibfm=TM00000&station_uid={STATION_UID}"
    announcements = fetch(url)

    print(f"{'line':<5} {'bus':<6} {'eta_min':<8} {'dist_km':<8} lat/lng")
    print("-" * 60)
    for a in announcements:
        # Station coordinates from the response
        lat0, lng0 = float(a["stations_gpsx"]), float(a["stations_gpsy"])
        for v in a.get("vehicles", []):
            lat, lng = float(v["lat"]), float(v["lng"])
            dist = haversine_km(lat0, lng0, lat, lng)
            print(f"{a['line_number']:<5} {v['garageNo']:<6} "
                  f"{a['seconds_left'] / 60:>6.1f}    {dist:>6.2f}    {lat:.5f},{lng:.5f}")


if __name__ == "__main__":
    main()