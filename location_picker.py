# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 02:13:39 2022

@author: Abhra
"""

import streamlit as st
from shapely.geometry import Point,Polygon
import geopandas as gpd
import pandas as pd
import geopy
import app
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

def generate_long_lat(a1,b1,c1,d1,a2,b2,c2,d2):
    
    #placeholder1= st.empty()
    sidebar1 = st.sidebar
    with sidebar1:
        st.write("Pickup location")
        street = st.text_input("Street", "Behala",key =a1)
        city = st.text_input("City", "Kolkata",key =b1)
        state = st.text_input("State", "Kolkata",key =c1)
        country = st.text_input("Country", "India",key=d1)
    
    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street+", "+city+", "+state+", "+country)
    
    lat = location.latitude
    lon = location.longitude
    
    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    placeholder2 = st.empty()
    placeholder2.map(map_data,zoom=12)
    
    placeholder3 = st.empty()
    isclick = placeholder3.button("Confirm pickup location",key="pick")
    if isclick:
        st.success("Pickup: {}".format(location))
        #del placeholder1
        del sidebar1
        del placeholder2
        long1,lat1 =lon,lat
        sidebar2 = st.sidebar
        with sidebar2:
            st.write("Dropoff location")
            street = st.text_input("Street", "Behala",key =a2)
            city = st.text_input("City", "Kolkata",key =b2)
            state = st.text_input("State", "Kolkata",key =c2)
            country = st.text_input("Country", "India",key=d2)
            
        geolocator = Nominatim(user_agent="GTA Lookup")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        location = geolocator.geocode(street+", "+city+", "+state+", "+country)
    
        lat = location.latitude
        lon = location.longitude
    
        map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
        st.map(map_data,zoom=12)
        long2,lat2 = lon,lat
        if st.button("Confirm dropoff location",key="drop"):
            st.success("Dropoff: {}".format(location))
            app.other_details(long1,lat1,long2,lat2)
            #return long1,lat1,long2,lat2
        


