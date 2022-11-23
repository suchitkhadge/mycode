#!/usr/bin/env python3
import requests
import pprint
import datetime
import reverse_geocoder as rg


URL= "http://api.open-notify.org/iss-now.json"
def main():
   resp= requests.get(URL).json()
   pprint.pprint(resp)
   print("CURRENT LOCATION OF THE ISS: ")
   print("Timestamp: ", datetime.datetime.fromtimestamp(resp["timestamp"]))
   print("Lon: ", resp["iss_position"]["longitude"])
   print("Lat: ", resp["iss_position"]["latitude"])

   # reverse_geocoder MUST be passed a tuple as the argument!
   coords_tuple= (resp["iss_position"]["latitude"], resp["iss_position"]["longitude"])
   result = rg.search(coords_tuple, verbose=False)
   print (result[0]["name"], ", ",result[0]["cc"])
if __name__ == "__main__":
    main()

