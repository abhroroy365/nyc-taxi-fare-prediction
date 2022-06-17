import numpy as np
import pandas as pd
import pickle
import calculations
import location_picker
import streamlit as st
import datetime
import time

pickle_in = open('classifier_final.pkl','rb')
classifier = pickle.load(pickle_in)
st.title("Cab Fare Prediction")
html_temp ="""
    <div style="background-color:tomato;padding:5px">
    <h3 style="color:white;text-align:center">Select on Map</h2>
    </div>
    <br>
    """
st.markdown(html_temp,unsafe_allow_html=True)

def predict_fare(pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,
                 passenger_count,pickup_datetime_year,pickup_datetime_month,
                 pickup_datetime_day,pickup_datetime_weekday,pickup_datetime_hour):
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
    return prediction
def main():
    placeholder = st.empty()
    @st.cache
    def btn():
        isclick = placeholder.button("Select location",key="select")
        return isclick
    if btn():
        placeholder.empty()
        with st.spinner("Here is your map"):
           location_picker.generate_long_lat("pick_street","pick_city","pick_state","pick_country",
                                             "drop_street","drop_city","drop_state","drop_country")
          
def other_details(pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude):
    passenger_count=st.slider("passenger_count",min_value =1,max_value=6)
    d = st.date_input(
     "Enter journey date",
     datetime.date(2022, 6, 11))
    pickup_datetime_year=d.year
    pickup_datetime_month=d.month
    pickup_datetime_day=d.day
    pickup_datetime_weekday=datetime.date(pickup_datetime_year, pickup_datetime_month, pickup_datetime_day).weekday()
    time_in = st.time_input(
        "Enter time",
        datetime.time(12,00,00))
    result=""
    pickup_datetime_hour = time_in.hour
    
    if st.button("predict"):
        result=predict_fare(pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,
                            passenger_count,pickup_datetime_year,pickup_datetime_month,
                            pickup_datetime_day,pickup_datetime_weekday,pickup_datetime_hour)
        st.success("The fare is around: {}".format(result))

if __name__=='__main__':
    main()
    