SQLAlchemy Climate Analysis and Flask API

Project Description:

This project involves conducting a climate analysis of Honolulu, Hawaii, utilizing Python, SQLAlchemy, Pandas, and Matplotlib. The analysis encompasses exploring climate data stored in a SQLite database and designing a Flask API based on the queries developed.

Instructions:

Database Connection:

Use SQLAlchemy's create_engine() function to connect to the SQLite database.
Utilize automap_base() to reflect tables into classes (measurement and station).
Establish a session to link Python to the database and ensure to close the session at the end.
Precipitation Analysis:

Retrieve the most recent date in the dataset.
Query the previous 12 months of precipitation data.
Save the results to a Pandas DataFrame, sort by date, and plot using Matplotlib.
Print summary statistics for the precipitation data.
Station Analysis:

Calculate the total number of stations in the dataset.
Identify the most-active stations and their observation counts.
Calculate the lowest, highest, and average temperatures for the most-active station.
Retrieve the previous 12 months of temperature observation (TOBS) data for the most-active station and plot a histogram.
Flask API Design:

Create routes for:
Homepage to list all available routes.
Precipitation data (/api/v1.0/precipitation).
Stations data (/api/v1.0/stations).
Temperature observations (/api/v1.0/tobs).
Minimum, average, and maximum temperatures for a given start or start-end range (/api/v1.0/<start> and /api/v1.0/<start>/<end>).
API SQLite Connection & Landing Page:

Ensure correct engine generation to the SQLite file.
Reflect the database schema using automap_base().
Save references to tables (measurement and station) and establish a session.
API Static Routes:

Implement routes to return JSON data for precipitation, stations, and temperature observations.
API Dynamic Route:

Create routes to accept start and start/end dates as parameters, and return JSON data for calculated temperature statistics.
Submission:

Reference:

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910. Link
