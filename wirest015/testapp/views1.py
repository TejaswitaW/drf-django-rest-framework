from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import io 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')  
class EmployeeCRUDCBV(View):
    # getting data
    def get(self,request,*args,**kwargs):
        json_data = request.body
        # getting json data
        stream = io.BytesIO(json_data)
        # converting into python native data type
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            # getting database object
            emp = Employee.objects.get(id=id)
            # convert this database object into python native datatype
            serializer = EmployeeSerializer(emp)
            # serilizer will give data in python datatype
            # converting that into json data
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json',status=200)
        # if id not provided, we have to send all data
        qs = Employee.objects.all()
        # using queryset
        serializer = EmployeeSerializer(qs,many=True)
        # converting qs to json
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    # creating new resource
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        # converting into python native data type
        pdata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            # internally called create method
            serializer.save()
            msg = {'msg':"Resource Created Successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        # same like form
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    # update data
    def put(self,request,*args,**kwargs):
        print("Inside put")
        json_data = request.body
        print("Inside put",json_data)
        stream = io.BytesIO(json_data)
        # converting into python native data type
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        print("Inside put",id)
        emp = Employee.objects.get(id=id)
        print("Inside put",emp)
        serializer = EmployeeSerializer(emp,data=pdata,partial=True)
        if serializer.is_valid():
            print("Inside put ins seri validation")
            serializer.save()
            msg = {'msg':"Resource Updated Successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        # converting into python native data type
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg':"Resource Deleted Successfully"}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')



    



