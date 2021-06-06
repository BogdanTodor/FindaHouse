# FindaHouse

### Scope of project
The project will start off as prototype built in Python with respects to the data engineering component of the project. As such, steps such as the data ingestion and transformation stages will be done within scraper.py. The goal is to transition the project into a cloud hosted solution using a batch processes approach where the entire ETL process is performed on AWS. 

The short term goal for the visualisation stage of the project is to have geopandas display the geospatial data locally for the prototype. However, long term the idea is to develop a front-end using Angular to provide a UI where users are able to input multiple suburbs and leaflet will visualise the result set with information available via popup markers on the map.

## Purpose 
subscribe to a list of suburbs you are interested in. scrape the data for the properties in those areas using python. Get their location via geocoding e.g. get address and then convert to lat/long. Use a mapping service to visualise where the properties are on the map. 

From here, we can create a heatmap for each suburb to identify suburbs with a large amount of sales vs a low amount of sales (**what question does this answer - potentially: which suburbs are difficult to break into?**).

Can also have a map looking at other important factors from the suburbs e.g. average number of town house complexes, gyms, shopping centres, bus stations etc nearby, train stations. (**Question answered: How much utility does the suburb give the buyer**).

Distance from CBD

**Evaluate factors that affect home insurance:**
* Home security (crime rate - https://www.police.qld.gov.au/maps-and-statistics) 
* Age and structure of property
* Natural hazard risk

**Datasets:**
* Cadastre data for local version / leaflet for the website version or even google maps api
* Real estate dot com data for the properties themselves
* {Investigate other sources}


***This is currently a draft***