from django.shortcuts import render
import requests

# Create your views here.
def get_geographic_info(request):
    # META is header information
    # if it is forwarded, we will get IP address from which request is coming, if it is not forwarded empty we are getting, empty means is False then second part will be considered,second one is the direct client IP address
    url = 'http://api.ipstack.com/124.40.246.61?access_key=2e54ab67c00d39a9482a3bad7e065205'
    response = requests.get(url)
    data = response.json()
    print(data)
    return render(request,'testapp/info.html',data)
