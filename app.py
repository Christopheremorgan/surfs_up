import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
import numpy as np

# access sqlite dbase and reflect it
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# class references of tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# create sqlite session link
session = Session(engine)

# create new Flask instance
app = Flask(__name__)

# define the starting point, for the welcome page root
@app.route('/')

def welcome():
    return (
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')

# build route for precipitation analysis
@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   # create a dictionary with the date as the key and the precipitation as the value and "jsonify" our dictionary
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# build route for station analysis
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    # unravel results into a one-dimensional array (note: jsonify argument changes with list)
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# build route for temperature analysis
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# build routes for temperature analysis (need to build for start and end dates)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# start and end dates to be called in the path sent to web browser (e.g. '.../api/v1.0/temp/2017-06-01/2017-06-30'
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # if not statement to determine start and end date, run this if no end date in url path
    if not end:
        # asterix is used here to denote that there will be multiple results for our query
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
