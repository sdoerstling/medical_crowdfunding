# Validation of a disease identification algorithm on medical crowdfunding campaigns

This repository contains source code for Doerstling et al (2021) *Validation of a disease identification algorithm on medical crowdfunding campaigns*.

----
## Overview of directories

- `code/` contains jupyter notebooks and python scripts
- `data/` contains raw and processed.
- `src/` contains utilities (e.g. dictionaries) imported by analysis scripts

----

## Data aggregation

### 1. GoFundMe Sitemap data 


### 2. CCSR data
- Download Clinical Classifications Software Refined (CCSR) for ICD-10-CM v2021.1 [here](https://www.hcup-us.ahrq.gov/toolssoftware/ccsr/DXCCSR_v2021-1.zip)
- Unzip and place contents in [data/ccsr](data/ccsr)

### 3. Language identification model
- Download Fasttext language identification model `lid.176.bin` [here](https://fasttext.cc/docs/en/language-identification.html)
- Place `lid.176.bin` fasttext model in [data/fasttext_models](data/fasttext_models)

----

## Scripts/notebooks

File | Description
--- | ---
`00-map_category_id.ipynb` <img width=200> | Scrapes example campaigns from each category in GoFundMe and identifies each category's numeric code (used during scraping).
 `01-prepare_sitemaps.ipynb` <img width=200>| Aggregates and randomizes sitemap data.

----

## Notes and disclaimers
- Data collection will vary
- Consider using a proxy, be respectful to server with scraping
- Consult your institutional review board
