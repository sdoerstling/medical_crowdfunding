# Medical crowdfunding third year project

This will serve as the repository for source code.

## To dos:

### Organization

### Data preparation and cleaning
-	Impact of adding stopwords to spark-jsl-ccsr on classification accuracy
-	Run spark-jsl_wip to have other options
-	if time, add county FIPS from zip code or location to add in census data
-	Infer disease categories from procedures or updates
  - after doing this, need to re-calculate categorization peformance because this will be included in our "pipeline"
- Need to figure out final inclusion/exclusion criteria, missing data percentage, etc.

- Retrace steps for manual revisions to CCSR
- start this from scratch because current version seems to leave out a lot (e.g. cerebral amyloid angiopathy)
- then re-test classification metrics from manual review to make sure we are kosher
- while I'm at this, figure out best way to exclude disease categories and calculated weighted precision, recall


### Visualizations
-	Distribution of financial variables by disease category
-	Histogram of donation amount
-	Histogram of average donation amount
-	Histogram of number of donations
- relationship between time and social media shares
- relationship between time and donations
- how long does it take for campaigns to reach 95% of their donations? 50% of goal amount?

### Analysis
-	Poisson regression of donation counts
-	Gamma regression of donation amounts
- Gamma? regression of amount requested

### Additional ideas – data preparation
-	Add procedures
- Accuracy of keras-mesh classifier?

### Additional ideas – analysis
-	Gender analysis of donor names to see who gives more frequently or more dollars
-	Impact of political affiliation of zipcode



# Notes
- shares were scraped on February 9, 2021


# Instructions

- Place lid.176.bin fasttext model in data/fasttext_models
