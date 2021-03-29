import requests
import json

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/"

team = input("Team football : ")

update_url = url + team

headers = {
    'x-rapidapi-key': "0d0d25d992msh3d89a140dd4e60ap113709jsnccdeba14d266",
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

response = requests.request("GET", update_url, headers=headers)

print(response.json())