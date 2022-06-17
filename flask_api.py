from flask import Flask,request
import numpy as np
import pandas as pd
import pickle
import flasgger
from flasgger import Swagger
import calculations

app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["GET"])
def predict_fare():
    
    """Predict the cab fare to desired location
    Hello
    ---
    parameters:
        - name: pickup_longitude
          in: query
          type: number
          required: True
        - name: pickup_latitude
          in: query
          type: number
          required: True
        - name: dropoff_longitude
          in: query
          type: number
          required: True
        - name: dropoff_latitude
          in: query
          type: number
          required: True
        - name: passenger_count
          in: query
          type: number
          required: True
        - name: pickup_datetime_year
          in: query
          type: number
          required: True
        - name: pickup_datetime_month
          in: query
          type: number
          required: True
        - name: pickup_datetime_day
          in: query
          type: number
          required: True
        - name: pickup_datetime_weekday
          in: query
          type: number
          required: True
        - name: pickup_datetime_hour
          in: query
          type: number
          required: True
          
    responses:
        200:
            description: The output values
        

    """
    pickup_longitude=request.args.get("pickup_longitude")
    pickup_latitude=request.args.get("pickup_latitude")
    dropoff_longitude=request.args.get("dropoff_longitude")
    dropoff_latitude=request.args.get("dropoff_latitude")
    passenger_count=request.args.get("passenger_count")
    pickup_datetime_year=request.args.get("pickup_datetime_year")
    pickup_datetime_month=request.args.get("pickup_datetime_month")
    pickup_datetime_day=request.args.get("pickup_datetime_day")
    pickup_datetime_weekday=request.args.get("pickup_datetime_weekday")
    pickup_datetime_hour=request.args.get("pickup_datetime_hour")
    
    distance = calculations.distance()
    travel_dist = distance.trip_distance(pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude)
    near = []
    near = distance.add_landmarks(dropoff_longitude, dropoff_latitude)
    lst = [[pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,
                                      passenger_count,pickup_datetime_year,pickup_datetime_month,
                                      pickup_datetime_day,pickup_datetime_weekday,pickup_datetime_hour,
                                      travel_dist,near[0],near[1],near[2],near[3],near[4],near[5]]]
    df = pd.DataFrame(lst,columns=['pickup_longitude', 'pickup_latitude',
       'dropoff_longitude', 'dropoff_latitude', 'passenger_count',
       'pickup_datetime_year', 'pickup_datetime_month', 'pickup_datetime_day',
       'pickup_datetime_weekday', 'pickup_datetime_hour', 'trip_distance',
       'JKF_drop_distance', 'LGA_drop_distance', 'EWR_drop_distance',
       'TME_drop_distance', 'MET_drop_distance', 'WTC_drop_distance'],dtype=float)
    prediction = classifier.predict(df)
    print(prediction)
    return "Your cab fare is "+str(prediction)


if __name__=='__main__':
    app.run()
    
    
    
    
    
    
    