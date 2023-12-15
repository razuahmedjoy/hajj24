import requests
import json

URL = "http://localhost:8000/tents/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    req = requests.get(url = ULR, data = json_data)
    data = req.json()
    print(data)

get_data()