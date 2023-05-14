import requests
import geocoder

r = requests.get("http://api.open-notify.org/iss-now.json")
iss_data = r.json()
ip = geocoder.ipinfo()
iss_location = list(iss_data["iss_position"].values())
if (iss_location[0] == ip.latlng[0]) and (iss_location[1] == ip.latlng[1]):
    print("ISS is right above you!")
    print(f"ISS location\nLatitude: {iss_location[0]}\nLongitude: {iss_location[1]}")
else:
    print("ISS isn't right above you.\n")
    print(f"ISS location\n\tLatitude: {iss_location[0]}\n\tLongitude: {iss_location[1]}")
    print(f"Yours location\n\tLatitude: {ip.latlng[0]}\n\tLongitude: {ip.latlng[1]}")