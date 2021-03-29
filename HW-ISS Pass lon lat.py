import urllib.parse
import requests
import json
from datetime import datetime

while True:
    location = input("Input location : ")
    if location[0] == '/':
        location = location[1::]
        key = "KOABF2PRyktMAoVAj2PSHA7mhsGYT4qa"
        main_api = "https://www.mapquestapi.com/geocoding/v1/address?"
        url = main_api + urllib.parse.urlencode({"key":key, "location":location})
        res = requests.get(url)
        result = res.json()
        lat_lng = result["results"][0]["locations"][0]["latLng"]

        main_api = "http://api.open-notify.org/iss-pass.json?"
        url = main_api + urllib.parse.urlencode({"lat":lat_lng["lat"], "lon":lat_lng["lng"]})
        res = requests.get(url)
        result = res.json()

        # print(result["response"][0]["risetime"])
        # print(result["response"][0]["duration"])
        message1 = "Latitude and Longtitude are " + str(lat_lng["lat"]) + " and " + str(lat_lng["lng"])
        message_send = location + " is located at " + message1 + "\n" + "ISS will pass " + datetime.fromtimestamp(result["response"][0]["risetime"]).strftime("%A, %B %d, %Y %I:%M:%S")
        access_token = "Yzk0MmE0ZTktNDkwZC00MDlmLTllNzItMTU1ZGNhZTk1MGRkNzVjZmI5YmMtOTVh_PF84_consumer"
        room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3"
        url = 'https://webexapis.com/v1/messages'
        headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'markdown': message_send}
        res = requests.post(url, headers=headers, json=params)
    else:
        break