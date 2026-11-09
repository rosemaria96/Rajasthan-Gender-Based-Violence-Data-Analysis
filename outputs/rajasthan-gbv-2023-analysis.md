# Gender-Based Violence in Rajasthan: 2023 District Analysis

## Executive summary

This analysis uses NCRB-reported crimes against women for Rajasthan in 2023. It combines the NCRB district-level data published through an Esri feature service with the Ministry of Home Affairs (MHA) state totals reported from *Crime in India*.

- Rajasthan recorded **45,450 cases** in 2023. The MHA time series shows 40,738 in 2021 and 45,058 in 2022: an **11.6% rise from 2021 to 2023**, with a much smaller **0.9% rise from 2022 to 2023**.
- The published 2023 district totals cover **41 districts** and sum to 45,450, matching the MHA state total.
- **Jaipur** recorded the largest number (4,636; 10.2% of the state total). Udaipur (2,083), Bhilwara (1,968), Alwar (1,943), and Jodhpur (1,902) follow. The five largest district counts together account for 27.6% of recorded cases.
- Among selected recorded offence heads, **cruelty by husband or relatives** was the largest (18,033), followed by assault with intent to outrage modesty (9,456), kidnapping/abduction of women (7,522), and rape (5,078). These categories should not be summed into a total: crime-head tables may overlap and do not necessarily partition the aggregate.
- These are **registered police cases**, not a count of all violence experienced. Higher recorded counts may reflect population, access to reporting, police registration practices, or actual incidence. Lower counts cannot be interpreted as greater safety.

## Questions and scope

The analysis asks where registered cases were concentrated in 2023 and which recorded offence heads contributed most to the published figures. It does not estimate prevalence, individual risk, or causal relationships. It is a one-year district snapshot; it does not make district-level year-on-year comparisons.

## State trend

| Year | Cases registered | Change from previous year |
|---|---:|---:|
| 2021 | 40,738 | — |
| 2022 | 45,058 | +10.6% |
| 2023 | 45,450 | +0.9% |

The two-year increase from 2021 to 2023 was 11.6%. These totals are from the MHA parliamentary answer citing NCRB *Crime in India* data. A rise in registered cases should be read as a rise in recorded reports; it does not by itself prove that underlying violence rose at the same rate.

## District counts

Top ten districts by number of reported cases in 2023:

| District | Cases | Share of state total |
|---|---:|---:|
| Jaipur | 4,636 | 10.2% |
| Udaipur | 2,083 | 4.6% |
| Bhilwara | 1,968 | 4.3% |
| Alwar | 1,943 | 4.3% |
| Jodhpur | 1,902 | 4.2% |
| Ganganagar | 1,804 | 4.0% |
| Ajmer | 1,764 | 3.9% |
| Bharatpur | 1,624 | 3.6% |
| Kota | 1,602 | 3.5% |
| Sikar | 1,483 | 3.3% |

Jaipur is much higher in absolute count than the next district. This is not a population-adjusted comparison, so it should not be interpreted as a ranking of relative prevalence or safety. The complete 41-district table is in the accompanying CSV.

## Selected offence heads

| NCRB offence head | Recorded cases in Rajasthan, 2023 |
|---|---:|
| Cruelty by husband or relatives | 18,033 |
| Assault on women with intent to outrage modesty | 9,456 |
| Kidnapping and abduction of women | 7,522 |
| Rape | 5,078 |
| Dowry deaths | 428 |
| Women-centric cyber-crime under IT Act | 225 |

These are counts from distinct NCRB table fields, not necessarily mutually exclusive components of the aggregate total. The small count under a particular law or crime head does not indicate low need: some support-seeking or violence may be recorded under other laws, not reported to police, or not captured in this administrative dataset.

## Implications for Vishakha

1. Use Jaipur’s high absolute case volume as a prompt to explore service capacity and referral pathways, not as proof that Jaipur is the least safe district.
2. Review the large number recorded under cruelty by husband or relatives alongside available counselling, legal support, shelter, and referral capacity. This offence head points to the importance of accessible responses to violence within family relationships.
3. Compare police data with Vishakha’s anonymized programme and referral data, where available, to identify unmet support needs. Administrative crime counts alone cannot identify service gaps.
4. Validate district-level patterns with local teams and community partners before choosing outreach priorities. Ask whether local trends reflect population, reporting awareness, access, or police recording practices.
5. In future monitoring, pair reported-case counts with service access indicators, response times, referrals completed, and survivor feedback, collected with informed consent and strong privacy safeguards.

## Methods and data quality

- **District data:** NCRB district crime fields for 2023, served by the Esri India Living Atlas layer “District Wise Crime Against Women.” The layer provides district names/codes and crime-head counts. The sum of its 41 Rajasthan district total fields (`totipcsll23`) is 45,450.
- **State trend:** MHA Rajya Sabha answer, “State/UT-wise Cases Registered under Crime against Women during 2021–2023,” citing NCRB *Crime in India*: Rajasthan 40,738 (2021), 45,058 (2022), 45,450 (2023).
- **Validation:** The same map layer’s 2022 district values sum to 46,222 across 34 populated district records, which does not match the official 2022 state total of 45,058. Therefore, 2022 district values were not used for geographic trend analysis. The 2023 district values match the official state aggregate.
- **No rate calculation:** I did not divide district counts by Census 2011 female population. The count years, district boundaries, and populations would not be sufficiently aligned for a defensible current district rate. Results are absolute counts only.
- **Classification:** NCRB categories and legal definitions can change. Comparisons across years require checking definitions and administrative boundaries; this analysis avoids district trend comparisons for that reason.

## Limitations and ethical use

NCRB data reflect cases registered by police. They omit unreported incidents and are affected by awareness, access to police, reporting willingness, registration rules, and classification. The district table includes a later district structure than the 2011 Census, so old Census denominators would not align cleanly. The analysis cannot explain why one district has more cases, establish causal links, or rank districts by women’s safety. Use aggregated information only; do not try to identify survivors or communities.

## Data and sources

- [MHA Rajya Sabha answer: cases registered against women, 2021–2023](https://www.mha.gov.in/MHA1/Par2017/pdfs/par2025-pdfs/RS03122025/390.pdf)
- [NCRB district feature service and field metadata, 2023 values](https://livingatlas.esri.in/server1/rest/services/NCRB/District_Wise_Crime_Against_Women_2022/MapServer/0)
- [NCRB Crime in India portal](https://www.ncrb.gov.in/)
- [Official India Open Government Data catalog: Crime in India 2022](https://tn.data.gov.in/catalog/crime-india-2022)
- [Rajasthan district-wise demography, Census 2011 (not used for current rates)](https://jankalyanfile.rajasthan.gov.in/Content/UploadFolder/DepartmentMaster/166/2024/Jul/30409/16686a99b93-9843-422a-8957-9be648dab526.pdf)

## Reproducibility

The accompanying CSV contains all 41 districts, total reported cases, share of the state total, and selected 2023 crime-head fields. State-level trend changes are calculated as `(current year / previous year - 1) × 100`. Counts and percentage shares are rounded only for display.
