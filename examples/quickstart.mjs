// Tutorial 4 — Live arrivals in Node.js (18+, global fetch).
// Run:  node quickstart.mjs
const API_KEY = "4670f468049bbee2260";
const BASE = "https://online.nsmart.rs";

async function getArrivals(stationUid, line = "TM00000") {
  const url = `${BASE}/publicapi/v1/announcement/announcement.php?ibfm=${line}&station_uid=${stationUid}`;
  const res = await fetch(url, { headers: { "X-Api-Authentication": API_KEY } });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

const arrivals = await getArrivals(6532, "7A");

if (Array.isArray(arrivals) && arrivals.length && "success" in arrivals[0]) {
  console.log("API error:", JSON.stringify(arrivals));
  process.exit(1);
}

for (const a of arrivals) {
  const etaMin = (a.seconds_left / 60).toFixed(1);
  const bus = a.vehicles?.[0];
  console.log(
    `Line ${a.line_number} · bus ${a.garage_no}` +
    (bus ? ` @ ${bus.lat},${bus.lng}` : "") +
    ` · ETA ${etaMin} min · ${a.station_name}`
  );
}