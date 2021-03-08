# Medical crowdfunding third year project

This will serve as the repository for source code.

## To dos:

### Organization

### Data preparation and cleaning


- add neighborhood deprivation index breakdown by census region (and also disease categories)

- also look at census variables by census region

- scrape other shares data that were not originally included

- run (additional) regressions with conditions

- co-occurrence matrix

- run algorithm on campaigns that did not make it in the first time


-	Infer disease categories from procedures or updates
  -	this adds almost 3k campaigns back in the mix 
  - after doing this, seems to slightly improve classification accuracy and F1
  - should definitely run spark-jsl_wip to have other options, this will likely improve sample size and performance
   - a potential extension could be taking all identified entities, and then use these as a word search based approach
      - Flow would be:
        1. spark-jsl on all documents
        2. gather all mapped terms, clean, lowercase, dictionary to mapped category (may be some terms mapped to multiple categories)
        3. word search over all documents
        4. then evaluate if more campaigns have an identified disease category
        5. if so, then see if that second pass impacts classification performance



### Visualizations
- relationship between time and social media shares
- relationship between time and donations
- how long does it take for campaigns to reach 95% of their donations? 50% of goal amount?

### Analysis
- quantify number of campaigns changed by winsorization 
- Need to figure out final inclusion/exclusion criteria, missing data percentage, etc.
- analyze missing data for number of shares

### Additional ideas – data preparation
-	Add procedures
- Accuracy of keras-mesh classifier?

### Additional ideas – analysis
-	Gender analysis of donor names to see who gives more frequently or more dollars
-	Impact of political affiliation of zipcode


# Notes
- shares were scraped on February 9, 2021
- census variables adapted from https://github.com/silverer/cancer-crowdfunding-explorer/blob/master/data/census/census_variables.csv
- census regions were obtained from https://github.com/cphalpert/census-regions/blob/master/us%20census%20bureau%20regions%20and%20divisions.csv
- census regions reference: https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf
- zip to county mapping data for the 4th quarter of 2020 were accessed from https://www.huduser.gov/portal/datasets/usps_crosswalk.html
- state FIPS codes were obtained from https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696


# Instructions
- Place lid.176.bin fasttext model in data/fasttext_models

# Exclusions
- 92962 unique urls
- 92118 with available location data that aligned with census data

#  Retrace steps for manual revisions to CCSR
- then re-test classification metrics from manual review to make sure we are kosher

- DXCCSR_v2021-1.CSV file was read in and cleaned of apostrophes. This maps ICD10 codes to categories
- DXCCSR-Reference-File-v2021-1.xlsx, sheet=CCSR_Categories was arranged into a hierarchy of disease categories inspired by groups provided in sheet=Naming_Conventions. Changes from the CCS-provided categories included recategorizing congenital conditions into the system impacted by the congenital anomaly.
- this disease hierarhcy was then merged with the ICD10-category mapping using the default inpatient CCSR category such that each ICD10 code could be mapped to an aggregated disease category




