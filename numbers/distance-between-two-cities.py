from geopy.geocoders import Nominatim
from math import sqrt,pow,pi,sin,cos,atan2

#finding longitude and latitude
def location(locA, locB):
    geolocator = Nominatim()
    get_locA = geolocator.geocode(locA)
    get_locB = geolocator.geocode(locB)
    Haversine(get_locA.latitude, get_locA.longitude, get_locB.latitude, get_locB.longitude)


#Haversine algorithm for distance calculation
def Haversine(lat_1, lon_1, lat_2, lon_2):
        degree_to_rad = float(pi / 180)
        lat = (lat_2 - lat_1) * degree_to_rad
        lon = (lon_2 - lon_1) * degree_to_rad
        a = pow(sin(lat / 2), 2) + cos(lat_1 * degree_to_rad) * cos(lat_2 * degree_to_rad) * pow(sin(lon / 2), 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        km = 6367 * c
        mi = 3956 * c
        print("Km: " + str(km) + "or miles " + str(mi))

def msg():
    inpt_1 = input("Distance between: ")
    inpt_2 = input("And: ")
    location(inpt_1, inpt_2)


msg()
