
import numpy as np
import math
import haversine
from haversine import haversine, Unit

class distance:
    
    def haversine_km(self,long1,lat1,long2,lat2):
           start = (lat1 ,long1)
           stop = (lat2 ,long2)
           return haversine(start,stop)

    def trip_distance(self,pickup_longitude,
                      pickup_latitude,
                      dropoff_longitude,
                      dropoff_latitude):
        travel_distance = self.haversine_km(pickup_longitude,
                                     pickup_latitude,
                                     dropoff_longitude,
                                     dropoff_latitude)
        return travel_distance
    
    def landmarks(self):
        jkf_longlat = (-73.7781, 40.6413)
        lga_longlat = (-73.8740, 40.7769)
        ewr_longlat = (-74.1745, 40.6895)
        tme_longlat = (-73.9855, 40.7580)
        met_longlat = (-73.9632, 40.7794)
        wtc_longlat = (-74.0099, 40.7126) 
        spots =    [jkf_longlat,
                    lga_longlat,
                    ewr_longlat,
                    tme_longlat,
                    met_longlat,
                    wtc_longlat]
        return spots
    
    def add_landmark_distance(self,land_longlat,dropoff_longitude,dropoff_latitude):
        long,lat = land_longlat
        d  =  self.haversine_km(long,
                                lat,
                                dropoff_longitude,
                                dropoff_latitude)
        return round(d,6)
    
    def add_landmarks(self,dropoff_longitude,dropoff_latitude):
        arr=[]
        spots = self.landmarks()
        for longlat in spots:
            arr.append(self.add_landmark_distance(longlat,dropoff_longitude,dropoff_latitude))
        return arr
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    