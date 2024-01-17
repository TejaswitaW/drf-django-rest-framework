import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

def get_resource(id):
    url = BASE_URL + ENDPOINT + str(id) + "/"
    print(url)
    R = requests.get(url)
    print(R.status_code)
    print(R.json())
    print(type(R.json()))


def get_all():
    url = BASE_URL + ENDPOINT

    R = requests.get(url)

    if R.status_code == 404:
        print("Resource not found")
    elif R.status_code == 200:
        print(R.json())
    else:
        print("Unexpected status code:", R.status_code)

def create_resource():
    new_emp = {
        'eno':119,
        'ename':"Kartiki K",
        'esal':400000,
        'eaddr':"Pune",
    }
    url = BASE_URL + ENDPOINT
    # we can send json data only
    new_emp = json.dumps(new_emp)
    resp = requests.post(url,data=new_emp)
    print(resp.status_code)
    print(resp.json())

def update_resource(id):
    new_emp = {
        'esal':40000000,
        'eaddr':"Gwalior",
    }
    url = BASE_URL + ENDPOINT + str(id) + "/"
    # we can send json data only
    new_emp = json.dumps(new_emp)
    resp = requests.put(url,data=new_emp)
    print(resp.status_code)
    print(resp.json())

def delete_resource(id):
    url = BASE_URL + ENDPOINT + str(id) + "/"
    resp = requests.delete(url)
    print(resp.status_code)
    print(resp.json())

#get_all()
#get_resource(1)
#create_resource()
# update_resource(1)
delete_resource(3)


