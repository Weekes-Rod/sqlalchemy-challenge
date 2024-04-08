from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create a Flask app instance
app = Flask(__name__)

# Create engine and reflect database tables
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link
session = Session(engine)

# Route to the homepage
@app.route('/')
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

# Route to retrieve precipitation data
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Calculate the date one year ago from the last date in database
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, '%Y-%m-%d').date() - dt.timedelta(days=365)
    
    # Query to retrieve precipitation data for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    
    # Convert the query results to a dictionary using date as the key and prcp as the value
    precipitation_data = {date: prcp for date, prcp in results}
    
    return jsonify(precipitation_data)

# Route to retrieve station data
@app.route('/api/v1.0/stations')
def stations():
    # Query to retrieve station data
    results = session.query(Station.station).all()
    
    # Convert the query results to a list
    station_data = [station[0] for station in results]
    
    return jsonify(station_data)

# Route to retrieve temperature observations for the previous year
@app.route('/api/v1.0/tobs')
def tobs():
    # Calculate the date one year ago from the last date in database
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, '%Y-%m-%d').date() - dt.timedelta(days=365)
    
    # Query to retrieve temperature observations for the last 12 months
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= one_year_ago).all()
    
    # Convert the query results to a list of dictionaries
    tobs_data = [{"date": date, "temperature": tobs} for date, tobs in results]
    
    return jsonify(tobs_data)

# Route to retrieve temperature statistics for a given start date
@app.route('/api/v1.0/<start>')
def temperature_stats_start(start):
    # Query to calculate temperature statistics for the specified start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).all()
    
    # Convert the query results to a dictionary
    temperature_stats = {"TMIN": results[0][0], "TAVG": results[0][1], "TMAX": results[0][2]}
    
    return jsonify(temperature_stats)

# Route to retrieve temperature statistics for a given start and end date
@app.route('/api/v1.0/<start>/<end>')
def temperature_stats_start_end(start, end):
    # Query to calculate temperature statistics for the specified start and end dates
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    # Convert the query results to a dictionary
    temperature_stats = {"TMIN": results[0][0], "TAVG": results[0][1], "TMAX": results[0][2]}
    
    return jsonify(temperature_stats)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
