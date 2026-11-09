Rajasthan Crimes Against Women Analysis

A reproducible, district-level analysis of NCRB-reported crimes against women in Rajasthan, using the latest year in the analysis: **2024**.

Project files

- `rajasthan-gbv-latest-2024-analysis.md` — findings, state trend, methods, and interpretation notes.
- `rajasthan_district_reported_crimes_2024.csv` — 2024 aggregate and selected crime-head counts for 41 districts.
- `analyze_rajasthan_gbv.py` — Python script that fetches the district data, checks the total, and writes the CSV.
- `rajasthan-gbv-2023-analysis.md` and `rajasthan_district_reported_crimes_2023.csv` — earlier-year analysis files.
- `rajasthan-gbv-data-analysis-project.md` — initial project brief and research plan.

Research question

How were police-registered crimes against women distributed across Rajasthan districts and selected offence categories in 2024?

Key 2024 findings

- The district dataset contains **36,563 cases** across 41 Rajasthan districts.
- Jaipur had the largest count, at **3,646** (10.0% of the state total).
- The largest selected offence head was cruelty by husband or relatives, with **10,578** recorded cases.
- These are absolute registered-case counts, not population-adjusted rates or estimates of total violence.

The report includes the state-level series for 2021–2024 and discusses the limits of interpreting year-to-year changes.

Data sources

1. District-level counts: NCRB-derived [District Wise Crime Against Women feature service](https://livingatlas.esri.in/server1/rest/services/NCRB/District_Wise_Crime_Against_Women_2022/MapServer/0). The service contains 2024 aggregate and crime-head fields for districts.
2. State-level 2021–2023 counts: Ministry of Home Affairs [Rajya Sabha answer No. 390](https://www.mha.gov.in/MHA1/Par2017/pdfs/par2025-pdfs/RS03122025/390.pdf), citing NCRB *Crime in India*.
3. NCRB 2024 catalogue: [Crime in India 2024 data catalogue](https://data.opencity.in/dataset/crime-in-india-2024).

Run the analysis

Requirements: Python 3 and an internet connection. The script uses only Python’s standard library; no package installation is required.

From this folder, run:

```powershell
python .\analyze_rajasthan_gbv.py
```

The script writes `rajasthan_district_reported_crimes_2024.csv` beside itself. To write to a different location, pass the desired CSV path:

```powershell
python .\analyze_rajasthan_gbv.py .\results\rajasthan_2024.csv
```

The script stops if the district totals do not add up to the expected **36,563**. This check helps catch changes in the source data; it does not validate every source field or establish that reported cases measure all incidents.

CSV fields

| Field | Description |
|---|---|
| `district` | District name as provided by the service |
| `reported_crimes_against_women_2024` | Aggregate registered cases, IPC/BNS and SLL categories |
| `share_of_state_reported_total_percent` | District count divided by 36,563, as a percent |
| `rape_cases_2024` | Rape cases recorded in the selected crime-head field |
| `cruelty_by_husband_or_relatives_2024` | Cases recorded under this offence head |
| `assault_intent_to_outrage_modesty_2024` | Cases recorded under this offence head |
| `kidnapping_abduction_women_2024` | Cases recorded under this offence head |
| `dowry_deaths_2024` | Cases recorded under this offence head |
| `sexual_harassment_2024` | Cases recorded under this offence head |
| `cyber_crimes_women_centric_2024` | Women-centric IT Act cases in the service field |
| `POCSO_girl_child_victim_cases_2024` | POCSO cases involving girl-child victims in the service field |

Crime-head fields are not necessarily mutually exclusive and should not be summed to recreate the aggregate total.

Interpretation and limitations

- NCRB figures count cases registered by police. They do not capture all violence or unreported incidents.
- Changes in reported cases may reflect reporting access, willingness to report, registration practices, classification, and underlying incidence.
- District counts are not rates. Current district boundaries do not align cleanly with older Census population denominators, so the analysis does not calculate district rates.
- A higher count does not by itself mean greater individual risk; a lower count does not prove greater safety.
- The 2024 criminal-law transition to BNS may affect comparisons with earlier years. The report presents the 2021–2024 series as context rather than a causal measure of changing prevalence.
- Do not use the district table to rank safety or infer causes. Use aggregated data and avoid any attempt to identify survivors or communities.

## Intended use

This is a portfolio and programme-planning analysis aligned with Vishakha’s work on violence prevention and women’s rights. Findings can suggest questions for further investigation, but should be checked with programme teams and community knowledge before guiding interventions.
