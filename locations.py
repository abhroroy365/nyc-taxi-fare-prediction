# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 00:56:46 2022

@author: Abhra
"""
import requests

ACCESS_FILE = open("api_key.txt","r")
ACCESS_KEY = ACCESS_FILE.read()
ACCESS_FILE.close()

def generate_long_lat(address1):
    address = address1
    param = {
        'access_token': ACCESS_KEY,
        }
    alist=[]
    base_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"+address+".json?"
    response = requests.get(base_url,params=param).json()
    alist = response['features'][0]['geometry']['coordinates']
    long,lat = round(alist[0],3),round(alist[1],3)
    print(long,lat)
    return long,lat   
