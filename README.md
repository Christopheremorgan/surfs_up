# surfs_up

## Analysis Overview
An entrepreneur wants to open a Surf & Shake shop in Oahu. Before investing his own savings he requires investor support and garnered interest from a Mr. W. Avy. Mr. Avy is a fan but has concern about weather as he invested in a surf shop early in his career and the shop closed after opening during a bad weather season.  He needs to see due diligence in our analysis on the viability of the business relative to the weather on the island.  If the first shop does well, the investor is interested in expanding the shop to other viable island locations.

Tools used for the analysis include the Python SQLAlchemy package coded within Jupyter notebooks to query a SQLite db with climate data for various weather stations across the islands.  To share the results of the analysis with an investment board via use of a browser, the Flask package in Python was used leveraging PyCharm as the IDE.


## Results
From the initial analysis performed for W. Avy we find that Hawaii is blessed with year round moderate temperatures with temperatures ranging between 70 and 80 degrees for most of the year.  

PREVIOUS YEAR TEMPERATURE HISTOGRAM
![image_name](https://github.com/Christopheremorgan/surfs_up/blob/main/PrevYrTempHisto.png)

Mr. Avy wants to provide additional due diligence for the board looking specifically at the months of June and December for the weather history we have available. The 3 key difference betwee June and December temperatures over multiple years:
* The minimum temperature in December, 56F, is 8 degrees lower than in June
* The inner quartile days for both months is tight with December being 3-4 degrees lower than June
* There is one additional year of data for June than for December, 2017

JUNE TEMPERATURE SUMMARY STATISTICS (2010 - 2017)
![image_name](https://github.com/Christopheremorgan/surfs_up/blob/main/JuneTemps.png)

DECEMBER TEMPERATURE SUMMARY STATISTICS (2010 - 2016)
![image_name](https://github.com/Christopheremorgan/surfs_up/blob/main/DecemberTemps.png)


## Summary
To provide a more holistic view of weather comparisons for June & December precipitation analysis is also provided.  Insights from the analysis indicate:
* recommendation one
* recommendation two
* recommendation three

PREVIOUS YEAR PRECIPITATION HISTOGRAM
![image_name](https://github.com/Christopheremorgan/surfs_up/blob/main/PrevYrTempHisto.png)

JUNE PRECIPITATION SUMMARY STATISTICS (2010 - 2017)
![image_name](https://github.com/Christopheremorgan/surfs_up/blob/main/JuneTemps.png)

DECEMBER PRECIPITATION SUMMARY STATISTICS (2010 - 2016)
![image_name](https://github.com/Christopheremorgan/surfs_up/blob/main/DecemberTemps.png)


## Coding & Resource Files
[SurfsUp_Challenge.ipynb](https://github.com/Christopheremorgan/Movies-ETL/blob/main/Resources/movies_metadata.csv.zip) 

[hawaii.sqlite](https://github.com/Christopheremorgan/Movies-ETL/blob/main/Resources/wikipedia-movies.json) 


