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
    new_emp = {
        'eno':184,
        'ename':"Teju K",
        'esal':300000,
        'eaddr':"Bengaluru",
    }
    url = BASE_URL + ENDPOINT
    # we can send json data only
    new_emp = json.dumps(new_emp)
    resp = requests.post(url,data=new_emp)
    print(resp.status_code)
    print(resp.json())

def update_resource(id=None):
    new_emp = {
        'id':id,
        'esal':12345000,
        'ename':"Kartiki",
    }
    url = BASE_URL + ENDPOINT 
    # we can send json data only
    new_emp = json.dumps(new_emp)
    resp = requests.put(url,data=new_emp)
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
#update_resource(3)
#delete_resource(1)


