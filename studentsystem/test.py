import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

def get_resource(id=None):
    data = {}
    if id:
        data = {
            'id':id
        }
    url = BASE_URL + ENDPOINT 
    R = requests.get(url,data=json.dumps(data))
    print(R.status_code)
    print(R.json())
   
def create_resource():
    new_std = {
        'name':"Virat K",
        'rollno':148,
        'marks':46,
        'gf':'A',
        'bf':'B',
    }
    url = BASE_URL + ENDPOINT
    # we can send json data only
    new_std = json.dumps(new_std)
    resp = requests.post(url,data=new_std)
    print(resp.status_code)
    print(resp.json())

def update_resource(id=None):
    new_std = {
        'id':id,
        'gf':"XYZ",
      }
    url = BASE_URL + ENDPOINT 
    # we can send json data only
    new_std = json.dumps(new_std)
    resp = requests.put(url,data=new_std)
    print(resp.status_code)
    print(resp.json())

def delete_resource(id=None):
    data = {
        'id':id,
    }
    url = BASE_URL + ENDPOINT
    data = json.dumps(data)
    resp = requests.delete(url,data=data)
    print(resp.status_code)
    print(resp.json())


get_resource()
#create_resource()
#update_resource()
#delete_resource(4)


