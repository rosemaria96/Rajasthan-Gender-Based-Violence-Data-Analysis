#!/usr/bin/env python3
"""Rebuild the 2024 Rajasthan crimes-against-women district analysis.

Uses the NCRB-derived Esri feature service and Python's standard library.
Run: python analyze_rajasthan_gbv.py [output.csv]
"""

from __future__ import annotations

import csv
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

SERVICE_URL = (
    "https://livingatlas.esri.in/server1/rest/services/NCRB/"
    "District_Wise_Crime_Against_Women_2022/MapServer/0/query"
)
YEAR = 2024
TOTAL_FIELD = "totcrwom24"
STATE_TOTAL = 36_563

# Output label => source field in the NCRB-derived service.
FIELDS = {
    "rape_cases_2024": "totrape24",
    "cruelty_by_husband_or_relatives_2024": "crlhus24",
    "assault_intent_to_outrage_modesty_2024": "totmod24",
    "kidnapping_abduction_women_2024": "totkidabd24",
    "dowry_deaths_2024": "dwydeath24",
    "sexual_harassment_2024": "totsexh24",
    "cyber_crimes_women_centric_2024": "totcyit24",
    "POCSO_girl_child_victim_cases_2024": "totpocso24",
}


def fetch_rajasthan_rows() -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "where": "state='Rajasthan'",
            "outFields": "*",
            "returnGeometry": "false",
            "f": "json",
        }
    )
    request = urllib.request.Request(
        f"{SERVICE_URL}?{params}",
        headers={"User-Agent": "RajasthanGBVAnalysis/1.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = json.load(response)

    if "error" in payload:
        raise RuntimeError(f"Esri service error: {payload['error']}")

    rows = [feature["attributes"] for feature in payload.get("features", [])]
    return [
        row
        for row in rows
        if row.get("state") == "Rajasthan"
        and isinstance(row.get(TOTAL_FIELD), (int, float))
    ]


def main() -> None:
    default_output = Path(__file__).with_name(
        "rajasthan_district_reported_crimes_2024.csv"
    )
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else default_output
    rows = fetch_rajasthan_rows()
    rows.sort(key=lambda row: (-row[TOTAL_FIELD], row.get("dis", "")))

    observed_total = sum(row[TOTAL_FIELD] for row in rows)
    if observed_total != STATE_TOTAL:
        raise SystemExit(
            f"Validation failed: district sum is {observed_total:,.0f}, "
            f"expected {STATE_TOTAL:,}. Check whether the source was updated."
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "district",
        "reported_crimes_against_women_2024",
        "share_of_state_reported_total_percent",
        *FIELDS.keys(),
    ]
    with output.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            record = {
                "district": row.get("dis", ""),
                "reported_crimes_against_women_2024": int(row[TOTAL_FIELD]),
                "share_of_state_reported_total_percent": round(
                    row[TOTAL_FIELD] / STATE_TOTAL * 100, 2
                ),
            }
            for label, source_field in FIELDS.items():
                record[label] = int(row.get(source_field) or 0)
            writer.writerow(record)

    print(f"Districts: {len(rows)}")
    print(f"District total: {observed_total:,.0f}")
    print(f"CSV written to: {output.resolve()}")
    print("Top 5 districts:")
    for row in rows[:5]:
        print(f"  {row['dis']}: {int(row[TOTAL_FIELD]):,}")
    print("Selected offence-head totals:")
    for label, source_field in FIELDS.items():
        print(f"  {label}: {sum(row.get(source_field) or 0 for row in rows):,}")


if __name__ == "__main__":
    main()
