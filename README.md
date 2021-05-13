# Validation of a disease identification algorithm on medical crowdfunding campaigns

This repository contains source code for Doerstling et al (2021) *Validation of a disease identification algorithm on medical crowdfunding campaigns*.

----

## Data collection

### 01. GoFundMe Sitemap data 


### 02. CCSR data
- Download Clinical Classifications Software Refined (CCSR) for ICD-10-CM v2021.1 [here](https://www.hcup-us.ahrq.gov/toolssoftware/ccsr/DXCCSR_v2021-1.zip)
- Unzip and place contents in [data/ccsr](data/ccsr)

### 03. Language identification model
- Download Fasttext language identification model lid.176.bin [here](https://fasttext.cc/docs/en/language-identification.html)
- Place lid.176.bin fasttext model in [data/fasttext_models](data/fasttext_models)

## Scripts/notebooks

File | Description
--- | ---
[code/00-map_category_id.ipynb](00-map_category_id.ipynb) | This scrapes example campaigns from each category in GoFundMe and identifies each category's numeric code.

----

## Notes and disclaimers
- 
