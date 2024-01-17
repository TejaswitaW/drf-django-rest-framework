from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.
def emp_data_view(request):
    emp_data = {
        'eno':100,
        'ename':'Tejaswita',
        'esal':300000,
        'eaddr' : 'Bengaluru'
    }

    resp = f"<h1>Name is {emp_data['ename']}<br>Employee number is {emp_data['eno']} <br>Employee salary is {emp_data['esal']}<br>Employee address is {emp_data['eaddr']}</h1>"

    # returning html reesponse which only browser can understand
    return HttpResponse(resp)

def emp_data_json_view(request):
    emp_data = {
        'eno':100,
        'ename':'Tejaswita',
        'esal':300000,
        'eaddr' : 'Bengaluru'
    }
    # convert python dictoinary to json
    json_data = json.dumps(emp_data)

    # returning json data in reponse which can be understood by any application
    return HttpResponse(json_data,content_type='application/json')

def emp_data_json_view_jsonresp(request):
    emp_data = {
        'eno':100,
        'ename':'Tejaswita',
        'esal':300000,
        'eaddr' : 'Bengaluru'
    }
    # converts dict into json object

    return JsonResponse(emp_data)