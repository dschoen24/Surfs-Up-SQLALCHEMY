# sqlalchemy-challenge

**Surfs Up!**

I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with my trip planning, I decided to do some climate analysis on the area. 

I used Python and SQLAlchemy to do some basic climate analysis and data exploration. All of the analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

**Precipitation Analysis**
•	I started by finding the most recent date in the data set.
•	Using this date, I retrieved the last 12 months of precipitation data by querying the 12 preceding months of data.
•	I then loaded the query results into a Pandas DataFrame and sorted the DataFrame values by date.
•	I plot these results using the DataFrame plot method.

My results for the precipitation data can be foound here: https://github.com/dschoen24/sqlalchemy-challenge/blob/main/Images/precip_analysis.png

**Station Analysis**
•	I designed a query to calculate the total number of stations present in the dataset provided.
•	I designed a query to find the most active stations within this data set and then listed the stations and observation counts in descending order.
  o	I figured out which station id has the highest number of observations
  o	Then, using the most active station id,  I calculated the lowest, highest, and average temperature.
•	I then designed a query to retrieve the last 12 months of temperature observation data (TOBS).
  o	I filtered by the station with the highest number of observations and queried the last 12 months of temperature observation data for this station.
  o	I then plot the results as a histogram.

My results for the station analysis can be found here: https://github.com/dschoen24/sqlalchemy-challenge/blob/main/Images/temp_vs_freq_histogram.png

Now that I have completed my initial analysis, I designed a Flask API based on the queries that I have just developed.

Now that I have completed my initial analysis, I designed a Flask API based on the queries that I have just developed.
**This FLASK API Code can be found here:** https://github.com/dschoen24/sqlalchemy-challenge/app.py

**Temperature Analysis II**
•  I am looking to take the trip from 8/1 to 8/7 of this year, but I am worried that the weather will be less than ideal. Using historical data from the dataset, I will find out what the temperature has previously looked like.
•  I used a function called calc_temps that will return the minimum, average, and maximum temperatures for the date range of my trip compared to the previous year.
•  Once I had these calvulations, I then ploted the min, avg, and max temperature as a bar chart.

My results can be found here: https://github.com/dschoen24/sqlalchemy-challenge/blob/main/Images/bonus_trip_avg_temp.png

**Daily Rainfall Average**
Now that I have an idea of the temperature, I will check to see what the rainfall has been, since I don't want it to rain the whole time I am there
  •	To get this information, I calculated the rainfall per weather station using the previous year's matching dates.
    o	I then sorted this data in descending order by precipitation amount and listed the station, name, latitude, longitude,       and elevation.
    
**Daily Temperature Normals**
•	I then calculated the daily normals for the duration of my trip. (Normals are the averages for the min, avg, and max temperatures).
•	To get this information, I performed the following:
  o	I set the start and end date of my trip.
  o	I created a range of dates.
  o	I striped off the year and saved a list of strings in the format %m-%d.
  o	I used the daily_normals function to calculate the normals for each date string and appended the results to a list.
•	I then loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.
•	I used Pandas to plot an area plot for these daily normals.

My results can be found here: https://github.com/dschoen24/sqlalchemy-challenge/blob/main/Images/bonus_daily_temp_normals.png






