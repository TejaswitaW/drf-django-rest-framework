from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from django.core.serializers import serialize
from .models import Employee
import json

class EmployeeDetailCBV(View):
    def get(self,request,id,*args,**kwargs):
        print("Inside get method: ",type(id))
        print(id)
        emp = Employee.objects.get(id=int(id))
        json_data = serialize('json',[emp,],fields=('eno','ename','eaddr'))
        return HttpResponse(json_data,content_type='application/json')

