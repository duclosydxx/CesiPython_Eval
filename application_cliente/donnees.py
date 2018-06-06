
import requests
import json


def GetDonnees():
    url="http://localhost:5000/json"
    r=requests.get(url)
    tabJSON = json.loads(r.text)
    return(tabJSON)