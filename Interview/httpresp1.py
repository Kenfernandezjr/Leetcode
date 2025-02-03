#!/usr/bin/env python3
import requests
import json
import csv

url = "https://api.pagerduty.com/services"

csvFile = input("Enter the name of the CSV file: ")
authorizationCode = input("Enter the authorization code: ")
listJson = []


#This code reads the CSV file and stores the data in a list
with open(csvFile, "r") as file:
    CSV_reader = csv.DictReader(file)
    for row in CSV_reader:
        listJson.append(row)

#This code converts the list to a JSON string
jsonString = json.dumps(listJson)

#This code sends the data to the PagerDuty API using the requests module
#loop through the list of services and send the data to the PagerDuty API in JSON format
for services in listJson:
    headers = {
 
    'Authorization': "Token token=" + authorizationCode,
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Content-Type': "application/json",
    }
    data = {
        "service": {
            "type": services["type"],
            "name": services["name"],
            "description": services["description"],
            "auto_resolve_timeout": services["auto_resolve_timeout"],
            "status": "active",
            "escalation_policy": {
                "id": "PLFXKDF",
                "type": "escalation_policy"
            },
        }
    }

    response = requests.post(url,headers=headers, json=data)

    if response.status_code == 201:
        print("Success: ", response)
    else:
        print("Error: ", response.status_code)
        print(response.json())  # This will print the error message
    