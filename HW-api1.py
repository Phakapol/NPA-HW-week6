import requests
import json

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

lon = float(input("lontitude : "))
lat = float(input("lattitude : "))

headers = {
    'x-rapidapi-key': "0d0d25d992msh3d89a140dd4e60ap113709jsnccdeba14d266",
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params={"lon": lon,"lat": lat})

print(response.json())