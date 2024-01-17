from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from .models import Employee
import json

class EmployeeDetailCBV(View):
    def get(self,request,id,*args,**kwargs):
        print(type(id))
        print("args: ",args)
        emp = Employee.objects.get(id=int(id))
        print("Datatype of emp: ",type(emp))
        emp_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr,
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data,content_type='application/json')

