Title: Dataframe Schema
Date: 2022-09-25 00:20
save_as: projects/dataframe_schema.html


**DataFrame Schema** is a small and slim package that does only one job - it checks if a given *DataFrame* fits certain list of defined expectation. It is heavily inspired by `jsonschema`, has only one dependency (Pydantic) and tries to be as simple and small as possible.

In our experience, we found that defining a very simple, explicit, and easy-to-generate definition of what we expect to get, is crucial in our day-to-day work.

## Core Ideas
Compared to the alternatives, this package has few cornerstone ideas:
1. It is meant to be simple and easy to use, taking minimal time to use and set up.
2. It puts *Dataframe* front and center and goes from there (Read more below)
3. It will be interchangable and will try to read  from and write to other formats (e.g. tableschema, great_expectations, etc).

   

## DataFrame in the middle 
We explicitly define "DataFrame" as a package-agnostic abstraction, as it (theoretically) could be a dataframe from *pandas,*, or *geopandas*, or *dask*, or *ray*, or *Spark*, or anything else. In each case, we use corresponding *flavor*, decision and assumptions made by the corresponding package. For example, if we check data derive from the database into pandas, we only care about datatype defined by *pandas*, and let it infer datatypes as it wish. 

> Right now we only support pandas, but it should be easy to add other flavors and it is on our roadmap.


## Resources
- [repository](https://github.com/StreetEasy/dfs)
- [pypi page](missing) 