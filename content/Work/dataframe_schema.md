Title: DataFrame Schema
Date: 2022-09-25 00:20
Slug: dataframe-schema

**DataFrame Schema** is a small and slim package that does only one job - it checks if a given *DataFrame* fits a certain list of defined expectations. It is heavily inspired by `jsonschema`, has only one dependency (Pydantic) and tries to be as simple and small as possible.

In our experience, we found that defining a very simple, explicit, and easy-to-generate definition of what we expect to get is crucial in our day-to-day work.

## Core Ideas
Compared to the alternatives, this package has a few cornerstone ideas:
1. It is meant to be simple and easy to use, taking minimal time to set up.
2. It puts *DataFrame* front and center and goes from there (read more below).
3. It will be interchangeable and will try to read from and write to other formats (e.g. tableschema, great_expectations, etc).

## DataFrame in the middle
We explicitly define "DataFrame" as a package-agnostic abstraction, as it (theoretically) could be a dataframe from *pandas*, or *geopandas*, or *dask*, or *ray*, or *Spark*, or anything else. In each case, we use the corresponding *flavor*, decisions, and assumptions made by that package. For example, if we check data derived from the database into pandas, we only care about the datatype defined by *pandas*, and let it infer datatypes as it wishes.

> Right now we only support pandas, but it should be easy to add other flavors, and it is on our roadmap.


## Resources
- [repository](https://github.com/StreetEasy/dfs)
- [pypi page](https://pypi.org/project/dataframe-schema/)
