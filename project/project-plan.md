# Project Plan

## Summary

This project aims to to examine the average number of bikes used in different areas and the need of new bicycle workshops based on number of bikes used in each area. we have bicycle riders data for each district in each hour and each day and in a different dataset of bicycle workshops where only bicycle are repaired or where both repaired, sold and rental offers. Furthermore, we have the dataset of the detailed address of the workshops (like phone number, zipcode etc.) of the bicycle workshop.


## Rationale


The analysis helps insights into the bike usage patterns across different areas. This analysis also helps to identify areas with higher bike usage, which could potentially indicate a higher demand for bicycle-related services like: bike workshops.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Mobilithek
* Metadata URL: https://mobilithek.info/offers/-8377471639463689219
* Data URL: https://opendata.stadt-muenster.de/dataset/verkehrsz%C3%A4hlung-fahrradverkehr-daten-der-z%C3%A4hlstellen-m%C3%BCnster-josefsviertel/resource/dbd8be87
* Data Type: XLSX

This dataset contains bike counting data for few years, both by the day and by the hour for Münster city.  Due to the volume of data, the counting points are divided by district. 

### Datasource2: GovData
* Metadata URL: https://www.govdata.de/web/guest/suchen/-/details/fahrradwerkstatten
* Data URL: https://geoserver.digitale-mrn.de/geoserver/metropolatlas/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=metropolatlas%3AMRN_OSM_shop_bycicle_repair_4326_Point&outputFormat=csv 
* Data Type: CSV

This dataset contains many bicycle workshops (where bicycle are sold, repaired, rents etc.) in different cities, countries with every possible details like phone number, zip code, address of the location.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Extract data from the databases
2. Analyze the dataset
3. Findings
4. Create graph
5. Draw conclusion

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
