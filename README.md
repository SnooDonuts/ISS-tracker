ISS Location Checker

This Python script retrieves the current location of the International Space Station (ISS) and compares it with your own location based on your IP address. It utilizes the requests library to fetch data from the "http://api.open-notify.org/iss-now.json" API, which provides the ISS's real-time position. The geocoder library is used to obtain your IP address's location.

If the ISS is directly above you, the script displays a message indicating its presence. Otherwise, it provides the latitude and longitude coordinates for both the ISS location and your own location.

This script serves as a fun way to check the relative proximity of the ISS to your current position.

Usage:
- Ensure that the requests and geocoder libraries are installed.
- Run the script to see the results in the console.

Note: The accuracy of the ISS location and your IP-based location may vary.
