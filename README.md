# example-for-aaron

Read this to learn about accessing NOAA data on ERRDAP

https://github.com/CoastWatch-WestCoast/ERDDAP-basics

https://coastwatch.noaa.gov/cwn/data-access-tools/coastwatch-data-portal.html

## Find some data

Go here and search chl
https://coastwatch.pfeg.noaa.gov/erddap/index.html

You'll need to find data that go back to 2010 when the oil spill happened and cover the gulf of mexico. This look pretty good

<img width="987" alt="image" src="https://user-images.githubusercontent.com/2545978/205971607-2acd5077-cc78-42d3-a312-26cf006dbde0.png">

Let's use the monthly product (because otherwise the data set will be massive) and go to graph so we can choose from a map.
https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMGchla3day.graph

I futz with the map until I get something like this. These data are at 4km resolution so the file would be massive it I did the whole Gulf.
<img width="405" alt="image" src="https://user-images.githubusercontent.com/2545978/205980465-7f4fc15c-d989-4ba2-9177-f6c26ff4a94e.png">

Now click the data access button so we can get the URL for downloading the data in csv format
<img width="178" alt="image" src="https://user-images.githubusercontent.com/2545978/205972912-c02a215d-6cca-4c93-b4a5-d9f4a67dd0bf.png">

I futz with the dates to be 1 years before and 1 years after. I also subsample for every 4th lat/long location so that the files are not so massive. I futzed around to get a file that was only 8 megabytes so that my example ran fast.
<img width="858" alt="image" src="https://user-images.githubusercontent.com/2545978/205981808-7be063c4-cbdd-4b4a-8378-623db27a1c42.png">

Go to the download part, select csv and generate the url.
<img width="861" alt="image" src="https://user-images.githubusercontent.com/2545978/205973517-ea9c0c09-9ee1-408b-82c3-015c14975992.png">
I click just generate the url since I will download the file with Python code.
Here is the URL
https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMGchlamday.csv?chlorophyll%5B(2009-04-16):1:(2011-04-16)%5D%5B(0.0):1:(0.0)%5D%5B(28.0):4:(30.8125)%5D%5B(-91.05):4:(-84.5)%5D

I take this url over to my Python file chl.py

