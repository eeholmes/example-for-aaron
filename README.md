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

I futz with the map until I get something like this.
<img width="441" alt="image" src="https://user-images.githubusercontent.com/2545978/205975793-c06fba0e-dd66-4891-8ed7-c31a82438cb5.png">

Now click the data access button so we can get the URL for downloading the data in csv format
<img width="178" alt="image" src="https://user-images.githubusercontent.com/2545978/205972912-c02a215d-6cca-4c93-b4a5-d9f4a67dd0bf.png">

I futz with the dates to be 2 years before and 2 years after. Hmm that might be a lot of data....
<img width="178" alt="image" src="https://user-images.githubusercontent.com/2545978/205973232-098b0bd1-dc5b-43a0-9833-da65a0ddfb3c.png">

Go to the download part and save as csv (or whatever).
<img width="861" alt="image" src="https://user-images.githubusercontent.com/2545978/205973517-ea9c0c09-9ee1-408b-82c3-015c14975992.png">
I click just generate the url since I will download the file with Python code.
Here is the URL
[https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMGchlamday.htmlTable?chlorophyll%5B(2008-02-15T12:00:00Z):1:(2012-05-16T12:00:00Z)%5D%5B(0.0):1:(0.0)%5D%5B(21.4):1:(29.6)%5D%5B(-91.6):1:(-83.4)%5D](https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMGchlamday.csv?chlorophyll%5B(2008-02-15T12:00:00Z):1:(2012-05-16T12:00:00Z)%5D%5B(0.0):1:(0.0)%5D%5B(21.4):1:(29.6)%5D%5B(-91.6):1:(-83.4)%5D)

I take this url over to my Python file chl.py

