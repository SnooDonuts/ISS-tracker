import requests
import geocoder
from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Radius of the Earth in kilometers
    radius = 6371.0

    # Calculate the differences between the latitudes and longitudes
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Apply the haversine formula
    a = sin(delta_lat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(delta_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c

    return distance

r = requests.get("http://api.open-notify.org/iss-now.json")
iss_data = r.json()
ip = geocoder.ipinfo()
iss_location = list(iss_data["iss_position"].values())
if (iss_location[0] == ip.latlng[0]) and (iss_location[1] == ip.latlng[1]):
    print("ISS is right above you!")
    print(f"ISS location\nLatitude: {iss_location[0]}\nLongitude: {iss_location[1]}")
else:
    print(f"ISS is cca {str(calculate_distance(float(iss_location[0]), float(iss_location[1]), float(ip.latlng[0]), float(ip.latlng[1])))}km from you\n")
    print(f"ISS location\n\tLatitude: {iss_location[0]}\n\tLongitude: {iss_location[1]}")
    print(f"Yours location\n\tLatitude: {ip.latlng[0]}\n\tLongitude: {ip.latlng[1]}")
