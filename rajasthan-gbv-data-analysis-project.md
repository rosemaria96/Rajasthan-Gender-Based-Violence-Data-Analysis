# Gender-Based Violence in Rajasthan: A District-Level Data Analysis

## Project brief

**Purpose.** Use publicly reported crime data to identify district-level patterns in crimes against women in Rajasthan and frame practical questions for outreach, prevention, and support services.

## Main question

How have reported crimes against women varied across Rajasthan districts and crime categories over time, and what can those patterns responsibly tell us about where further outreach or investigation may be useful?

### Supporting questions

1. Which crime categories account for the largest shares of recorded cases?
2. How have reported totals and category-specific counts changed over time?
3. Which districts have high or rising recorded counts, after accounting for population where compatible denominators are available?
4. Do results change when districts are grouped by rural/urban composition or female literacy, using Census 2011 indicators?

## Data plan

|Source|Use|Coverage / limitation|
|-|-|-|
|NCRB, *Crime in India* (district-level crimes against women by crime head), accessed through the District Crimes dataset|Annual reported case counts by reporting unit, district and crime head|Dataset page describes coverage from 2001–2024. It is a structured republication of NCRB data, so final figures should be checked against NCRB source tables. District boundaries and reporting units change over time.|
|Government of Rajasthan, *Economic Review 2023–24*, Appendix 29: District-wise Demography, Census 2011|Female population, rural/urban population and female literacy by the then-existing districts|Census 2011 is old and districts have since changed. Use for clearly labeled historical denominators or contextual comparison only; do not present as current population rates.|
|NCRB *Crime in India 2022* catalog on India’s Open Government Data platform|Official catalog / provenance for the NCRB annual publication|This catalog is an official source reference; it does not by itself provide a convenient analytical district CSV in the page view.|

**Source links**

* District Crimes dataset: https://distcrimes.dataful.in/datasets/2/
* NCRB source portal: https://www.ncrb.gov.in/
* India Open Government Data catalog for *Crime in India 2022*: https://tn.data.gov.in/catalog/crime-india-2022
* Rajasthan government demographic appendix (Census 2011): https://jankalyanfile.rajasthan.gov.in/Content/UploadFolder/DepartmentMaster/166/2024/Jul/30409/16686a99b93-9843-422a-8957-9be648dab526.pdf

## Analysis plan

1. **Set a comparable period.** Begin with the years for which Rajasthan district definitions and crime categories can be reconciled consistently. A 2014–2022 window is a reasonable first candidate; confirm it against the source tables before calculation.
2. **Keep reporting units distinct.** Include only district-level units for district comparisons. Treat commissionerates, railway police, cyber units, and other specialized units separately unless source documentation explicitly supports a non-overlapping district aggregation. This avoids double counting.
3. **Harmonize geography and labels.** Create a crosswalk for district names and boundary changes. Aggregate to stable historical geographies only where the source permits defensible mapping; mark non-comparable cases.
4. **Analyze counts first.** Show total reported cases and selected categories (for example, cruelty by husband or relatives, rape, kidnapping/abduction, assault, dowry deaths, and other recorded categories), plus year-on-year changes.
5. **Use rates cautiously.** A rate requires a population denominator matching the crime year, district boundaries, and population definition. Census 2011 female population alone cannot support current-year district crime rates. If compatible official projections are unavailable, show counts and avoid implying that counts equal risk.
6. **Compare with contextual indicators.** Where valid, explore associations with female literacy and rural/urban composition. Describe these as correlations, not causes.
7. **Validate with local knowledge.** Review apparent outliers with Vishakha’s staff or community partners before making service-planning recommendations.

## Planned outputs

* A short report (6–8 pages) with methods, findings, charts, limitations, and recommendations.
* A district-by-year table and category trend charts.
* A simple district map only if district boundaries and data can be harmonized reliably.
* A one-page briefing for programme teams, with questions for field validation.

## Interpretation and safeguards

NCRB figures count cases registered with police, not all incidents of gender-based violence. Differences can reflect population size, awareness, access to police, willingness to report, registration practices, law changes, and district boundary or reporting-unit changes. A lower count must never be described as proof that a district is safer. Avoid ranking communities as “unsafe” on raw counts, identifying survivors, or drawing causal conclusions from ecological comparisons. Publish aggregated results only.

## Current status and next data requirement

The sources and analysis design are identified, but numerical findings are not included in this brief. The dataset page exposes a downloadable CSV/XLSX interface, while direct automated retrieval was blocked during this work session. To complete the calculations, provide the downloaded NCRB district dataset (CSV/XLSX) or the call’s supplied dataset. The requested source is large (over 529,000 rows across India and years), so a filtered Rajasthan extract is also sufficient if it retains year, reporting unit, district, unit type, crime head, and value.

## Suggested proposal summary

This project will analyze NCRB-reported crimes against women across Rajasthan districts to understand recorded patterns by year and crime category. It will document changes in reporting units and district boundaries, avoid treating registered cases as a measure of total prevalence, and use compatible government population/context data only where valid.

