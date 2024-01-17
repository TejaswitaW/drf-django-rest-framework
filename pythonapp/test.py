import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

def get_resource(id):
    print("Get resource called")
    url = BASE_URL + ENDPOINT + str(id) + "/"
    print(url)
    R = requests.get(url)

    if R.status_code == 404:
        print("Resource not found")
    elif R.status_code == 200:
        print(R.json())
    else:
        print("Unexpected status code:", R.status_code)

def get_all():
    url = BASE_URL + ENDPOINT

    R = requests.get(url)

    if R.status_code == 404:
        print("Resource not found")
    elif R.status_code == 200:
        print(R.json())
    else:
        print("Unexpected status code:", R.status_code)

get_all()



