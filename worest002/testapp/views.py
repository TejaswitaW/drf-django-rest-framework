from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
import json

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data = {
        'eno':100,
        'ename':'Tejaswita W',
        'esal':3000000,
        'eaddr' : 'Bengaluru'
        }
        return JsonResponse(emp_data)
    def post(self,request,*args,**kwargs):
        emp_data = {
        'eno':100,
        'ename':'Tejaswita W',
        'esal':3000000,
        'eaddr' : 'Bengaluru'
        }
        return JsonResponse(emp_data)
    def put(self,request,*args,**kwargs):
        emp_data = {
        'eno':100,
        'ename':'Tejaswita W',
        'esal':3000000,
        'eaddr' : 'Bengaluru'
        }
        return JsonResponse(emp_data)
    def delete(self,request,*args,**kwargs):
        emp_data = {
        'eno':100,
        'ename':'Tejaswita W',
        'esal':3000000,
        'eaddr' : 'Bengaluru'
        }
        return JsonResponse(emp_data)





