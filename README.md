# Medical crowdfunding third year project

This will serve as the repository for source code.

## To dos:

### Organization

### Data preparation and cleaning


- check if feed_chunk json files does not include any data for final analysis
  - check in analysis notebook
  - if there were some left out, need to re-run 

-	Impact of adding stopwords to spark-jsl-ccsr on classification accuracy

-	Run spark-jsl_wip to have other options


-	Infer disease categories from procedures or updates
  - after doing this, need to re-calculate categorization peformance because this will be included in our "pipeline"

- Need to figure out final inclusion/exclusion criteria, missing data percentage, etc.

- Retrace steps for manual revisions to CCSR
  - for documentation in methods
  - and also because there are some missing sections to add to existing categories
  - start this from scratch because current version seems to leave out a lot (e.g. cerebral amyloid angiopathy)

- then re-test classification metrics from manual review to make sure we are kosher
  - while I'm at this, figure out best way to exclude disease categories and calculated weighted precision, recall
  
- quantify number of campaigns changed by winsorization 


### Visualizations
- relationship between time and social media shares
- relationship between time and donations
- how long does it take for campaigns to reach 95% of their donations? 50% of goal amount?

### Analysis

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
