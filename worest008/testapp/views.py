from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .mixins import SerializeMixin,HttpResponseMixin
from .models import Employee
from .utils import is_json
from .forms import EmployeeForm

@method_decorator(csrf_exempt,name='dispatch')  
class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=int(id))
        except Employee.DoesNotExist:
            emp = None
        return emp
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=int(id))
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'Employee does not exist'})
            return self.render_to_http_response(json_data,404)
        else: 
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)
        
    def put(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(int(id))
        if emp is None:
            json_data = json.dumps({'msg':'Employee does not exist to perform updation'})
            return self.render_to_http_response(json_data,404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please send valid json data only"})
            return self.render_to_http_response(json_data,status=400)
        # data got in post request
        provided_data = json.loads(data)
        # creating object using orginal data
        original_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        # updating original data with provided data
        original_data.update(provided_data)
        # here instance argument should be there,else new object will get created
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save()
            json_data = json.dumps({"msg":"Resource updated successfully"})
            return self.render_to_http_response(json_data)
        # if error come in form validation following code will get executed
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)  

    def delete(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(int(id))
        if emp is None:
            json_data = json.dumps({'msg':'Employee does not exist to perform deletion'})
            return self.render_to_http_response(json_data,404)  
        status,deleted_item = emp.delete()
        print(status,deleted_item)
        if status == 1:
            json_data = json.dumps({"msg":"Resource deleted successfully"})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({"msg":"Unable to delete..plz try again"})
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
        


