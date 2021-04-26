# Medical crowdfunding third year project

This will serve as the repository for source code.

# Tweedie regression
- https://stackoverflow.com/questions/63726276/statsmodel-tweedie-loglike-returning-nans
- https://towardsdatascience.com/insurance-risk-pricing-tweedie-approach-1d71207268fc
- Dunn and Smyth (2018), Generalized Linear Models With Examples in R
- https://stats.stackexchange.com/questions/123598/tweedie-p-parameter-interpretation

# GLM regression coefficient interpretation
- https://stats.stackexchange.com/questions/247309/interpretting-coefficients-of-a-glm-as-multiplicative
- https://stats.stackexchange.com/questions/96972/how-to-interpret-parameters-in-glm-with-family-gamma

# Notes
- shares were scraped on February 9, 2021
- census variables adapted from https://github.com/silverer/cancer-crowdfunding-explorer/blob/master/data/census/census_variables.csv
- census regions were obtained from https://github.com/cphalpert/census-regions/blob/master/us%20census%20bureau%20regions%20and%20divisions.csv
- census regions reference: https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf
- zip to county mapping data for the 4th quarter of 2020 were accessed from https://www.huduser.gov/portal/datasets/usps_crosswalk.html
- state FIPS codes were obtained from https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696

# Instructions
- Place lid.176.bin fasttext model in data/fasttext_models

# Notes on census
- Our data has zip codes
- However, using the same zip code listed by the campaign organizer for the patient assumes they live in the same zip code, which is a relatively small geographric area.
- Therefore, we generalize location to the county-level.


