from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .mixins import SerializeMixin,HttpResponseMixin
from .models import Employee
from .utils import is_json
from .forms import EmployeeForm


class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=int(id))
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'Employee does not exist'})
            return self.render_to_http_response(json_data,404)
        else: 
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)

@method_decorator(csrf_exempt,name='dispatch')  
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)
    
    def post(self,request,*args,**kwargs):
        # to get data from partner application
        data = request.body
        # print(data)
        # first checking is it valid json data or not
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please send valid json data only"})
            return self.render_to_http_response(json_data,status=400)
        # converting json data to python dictionary
        emp_data = json.loads(data)
        # creating form object using data recived
        form = EmployeeForm(emp_data)
        # checking form validation
        if form.is_valid():
            form.save()
            json_data = json.dumps({"msg":"Resource created successfully"})
            return self.render_to_http_response(json_data)
        # if error come in form validation following code will get executed
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

