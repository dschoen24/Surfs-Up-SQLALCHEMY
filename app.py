# Import Flask
from flask import Flask, jsonify

# Dependencies and Setup
import numpy as np
import datetime as dt

# Python SQL Toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool

# Database Setup
##############################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask Setup
##############################
app = Flask(__name__)

# Flask Routes
# Home Route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end (enter as YYY-MM-DD/YYYY-MM-DD)"
    )

# Convert the query results to a dictionary using "Date" as the key and "PRCP" as the value
@app.route("/api/v1.0/precipitation")
def precipitation():
# # Calculate the Date 1 Year Ago from the Last Data Point in the Database
# year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
# # Create query to retrieve the last 12 months of Precip data selecting only date & prcp
# prcp_data = session.query(measurement.date, measurement.prcp).\
#     filter(measurement.date >. year_ago).\
#     order_by(measurement.date).all()


    #Create session (link) from Python to the DB
    session = Session(engine)

    # Query measurement
    results = (session.query(measurement.date, measurement.prcp)
                .order_by(measurement.date))

# Create a dictionary of the results

