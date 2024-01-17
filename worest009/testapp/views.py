from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .mixins import SerializeMixin,HttpResponseMixin
from .models import Employee
from .utils import is_json
from .forms import EmployeeForm

# implementing single end point api, single view for CRUD
@method_decorator(csrf_exempt,name='dispatch') 
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=int(id))
        except Employee.DoesNotExist:
            emp = None
        return emp
    
    def get(self,request,*args,**kwargs):
        # first getting client provided data
        data = request.body
        # checking valid json or not
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please send valid json data only"})
            return self.render_to_http_response(json_data,status=400)
        # if valid json convert to python dictionary
        p_data = json.loads(data)
        # getting id from dictionary
        id = p_data.get('id',None)
        # getting employee object
        if id:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg':'No resource found with matched id'})
                return self.render_to_http_response(json_data,status=404)
            # if employee data found sending back to partner application
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)
        # if id not provided send all employee data
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

    def put(self,request,*args,**kwargs):
        # first getting client provided data
        data = request.body
        # checking valid json or not
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please send valid json data only"})
            return self.render_to_http_response(json_data,status=400)
        # if valid json convert to python dictionary
        p_data = json.loads(data)
        # getting id from dictionary
        id = p_data.get('id',None)
        # getting employee object
        if id is None:
            json_data = json.dumps({'msg':'To perform operation id is manadatory,please provide'})
            return self.render_to_http_response(json_data,status=400)
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({"msg":"The requested resource is not available"})
            return self.render_to_http_response(json_data,status=404)
        # now emp is available
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

    def delete(self,request,*args,**kwargs):
        # first getting client provided data
        data = request.body
        # checking valid json or not
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please send valid json data only"})
            return self.render_to_http_response(json_data,status=400)
        # if valid json convert to python dictionary
        p_data = json.loads(data)
        # getting id from dictionary
        id = p_data.get('id',None)
        # getting employee object
        if id is None:
            json_data = json.dumps({'msg':'To perform operation id is manadatory,please provide'})
            return self.render_to_http_response(json_data,status=400)
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({"msg":"The requested resource is not available"})
            return self.render_to_http_response(json_data,status=404)
        status,deleted_item = emp.delete()
        #print(status,deleted_item)
        if status == 1:
            json_data = json.dumps({"msg":"Resource deleted successfully"})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({"msg":"Unable to delete..plz try again"})
        return self.render_to_http_response(json_data)
        
    

        





