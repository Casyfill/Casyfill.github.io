Title: MosPlus (PlutoPlus copycat)
Date: 2020-09-27 20:58
save_as: projects/mosplus.html


**MosPlus** is a forked version of of Cris Wong's awesome [PlutoPlus](http://chriswhong.github.io/plutoplus/) project, built using open footprints for Moscow (Russia).

Building Footprint is a great Moscow Open Data Resource that contains a wealth of information about the city's building footprints, including address, cadaster zoning, status, registration data, and few more attributes.It contains information for the city's 145,000+ buildings, and includes 19 attributes for each one. That is (so far) a unique open data collection for Russia!

Moscow Building Footprint is quite large, available **only** through [API](http://api.data.mos.ru/) and hard to use. That is why I forked and edited blueprints for PlutoPlus, a great tool from Chris Wong (originally for **MapPluto** dataset) to to help people get access to smaller chunks of the data quickly and easily for whatever they are working on.
All data is version from *25.03.2016* and can be exported as *geoJSON*, *zipped shapefile*, and *CSV*, or can be *imported directly to your cartoDB account*. Geometries are exported in *WGS84* (Latitude and Longitude). For neighborhood (rayon) borders, I used [this dataset](http://gis-lab.info/qa/moscow-atd.html) from Gis-Lab.

> Note: FYI, There is a separate, not-exactly-opensourced yet invaluable dataset in the wild, **data for ALL Buildings in Russia** including address, year, type, number of units and floors - so pretty similar to *Pluto*, originated on *reforma-zkh* website. It was since removed, but can be found on the the interned.

![screenshot](../static/mosplus.png)


## Links
- [repo](https://github.com/Casyfill/mosplus)
- [original PlutoPlus](http://chriswhong.github.io/plutoplus/#)

### Data
- [Brief Description(rus)](http://data.mos.ru/opendata/1927/description?versionNumber=1&releaseNumber=1)
- [Dataset Passport](http://data.mos.ru/opendata/1927/passport?versionNumber=1&releaseNumber=1)
- [Dataset](http://data.mos.ru/opendata/1927/data/table?versionNumber=1&releaseNumber=1)

