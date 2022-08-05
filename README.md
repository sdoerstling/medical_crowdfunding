# A Disease Identification Algorithm for Medical Crowdfunding Campaigns: Validation Study

This repository contains source code for Doerstling et al (2022) *A Disease Identification Algorithm for Medical Crowdfunding Campaigns: Validation Study*.

- Title: A Disease Identification Algorithm for Medical Crowdfunding Campaigns: Validation Study
- Authors: Doerstling SS, Akrobetu D, Engelhard MM, Chen F, Ubel PA
- Journal: Journal of Medical Internet Reserach
- DOI: [10.2196/32867](https://doi.org/10.2196/32867)
- PMID: [35727610](https://www.ncbi.nlm.nih.gov/pubmed/35727610)
- URL: https://www.jmir.org/2022/6/e32867

----
## Overview of directories

- [code/](code/) contains jupyter notebooks and python scripts
- [data/](data/) contains some data and directories for additional data collection described below
- [src/](src/) contains utilities and tokens referenced by analysis scripts

----

## Data aggregation

### 1. GoFundMe Sitemap data 
- Go to www.gofundeme.com/sitemap.xml
- Each sitemap file can be iteratively downloaded at the following url: https://www.gofundme.com/sitemaps/www/sitemapN.xml.gz where N is a number starting at 1
- Download all available files by incrementing N by 1 until the url returns an error
- Place files in [data/sitemaps/sitemaps_raw](data/sitemaps/sitemaps_raw)

### 2. CCSR data
- Download Clinical Classifications Software Refined (CCSR) for ICD-10-CM v2021.1 [here](https://www.hcup-us.ahrq.gov/toolssoftware/ccsr/DXCCSR_v2021-1.zip)
- Unzip and place contents in [data/ccsr](data/ccsr)

### 3. Language identification model
- Download Fasttext language identification model `lid.176.bin` [here](https://fasttext.cc/docs/en/language-identification.html)
- Place `lid.176.bin` fasttext model in [data/fasttext_models](data/fasttext_models)

### 4. HUD zip code to county crosswalk data
- Navigate to the HUD website [here](https://www.huduser.gov/portal/datasets/usps_crosswalk.html)
- At the bottom of the page, select the "Data" tab
- For crosswalk type, select "ZIP-COUNTY"
- For data year and quarter, select "4th Quarter 2020"
- Place the file in [data/census](data/census)

----

## Scripts/notebooks

File | Description
--- | ---
`00-map_category_id.ipynb` <img width=300/> | Scrapes example campaigns from each category in GoFundMe and identifies each category's numeric code (used during scraping).
`01-prepare_sitemaps.ipynb` <img width=300/> | Aggregates and randomizes sitemap data. Export lists of urls in batches of 1000 for the purposes of our scraping procedure, but this can be adjusted for your system's limitations or capacity.
`02-run_scrape.sh` <img width=300/> | Iteratively runs `03-scrape.py` on lists of urls from the sitemap data. The number of files to scrape in the loop can be specified in the script.
`03-scrape.py` <img width=300/> | Asynchronously scrapes feed, donation, comments, and updates from GoFundMe urls. Exports data as .json files.
`04-make_db.py` <img width=300/> | Creates sqlite databse.
`05-scrape_to_db.py` <img width=300/> | Dumps scraped data from .json files to sqlite database.
`06-clean_data.ipynb` <img width=300/> | Cleans data. You will need a US Census API key: sign up [here](https://api.census.gov/data/key_signup.html). Place your census key in `tokens.py` in [src/](src/).
`06-PCA.R` <img width=300/> | Runs PCA to calculate neighborhood deprivation index. Code is courtesy of [Silver et al](https://github.com/silverer/cancer-crowdfunding-explorer/blob/master/R/clustr.R).
`07-disease_categories.ipynb` <img width=300/> | Modifies CCSR data to create disease categories for ICD-10-CM codes.
`08-Spark-JSL.ipynb` <img width=300/> | Executes named entity recognition and entity resolution using models from Spark NLP for Healthcare (John Snow Labs). Requires a [license or demo](https://www.johnsnowlabs.com/spark-nlp-health/). Recommend running on Google Colab. Place data in [data/disease_categorization](data/disease_categorization) when finished.
`09-cohens_kappa.ipynb` <img width=600/> | Calculates Cohen's kappa between coders for each disease category encountered in the reference set campaign descriptions.
`10-evaluation_and_analysis.ipynb` <img width=600/> | Aggregates algorithm output data, calculates classification performance metrics, and reproducibly generates figures, tables, and appendices.


----

## Notes and disclaimers
- Because campaigns are constantly being added to/removed from GoFundMe, variation in scraped samples is expected.
- Adhere to best practices for web scraping (do not overwhelm servers, limit concurrent requests from a single IP address, consider a proxy, etc). 
- Consult your institutional review board before collecting data with the methods described above.
- `acs_variables.csv` is courtesy of [Silver et al](https://github.com/silverer/cancer-crowdfunding-explorer/blob/master/data/census/census_variables.csv)
