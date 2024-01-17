from django.http import HttpResponse
from django.views.generic import View
from .mixins import SerializeMixin,HttpResponseMixin
from .models import Employee
import json


class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            # exception handling if object does not exist
            emp = Employee.objects.get(id=int(id))
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'Employee does not exist'})
            # return HttpResponse(json_data,content_type='application/json',status=404)
            return self.render_to_http_response(json_data,404)
        else: 
            json_data = self.serialize([emp,])
            # json_data = serialize('json',[emp,],fields=('eno','ename','eaddr'))
            # return HttpResponse(json_data,content_type='application/json',status=200)
            return self.render_to_http_response(json_data)
    
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        # json_data = serialize('json',qs)
        # pdict = json.loads(json_data)
        # final_list = []
        # # to remove extra meta data, now getting only employee data
        # for obj in pdict:
        #     emp_data = obj['fields']
        #     final_list.append(emp_data)
        # json_data = json.dumps(final_list)
        # return HttpResponse(json_data,content_type='application/json')
        return self.render_to_http_response(json_data)

