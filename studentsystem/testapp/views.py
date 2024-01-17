from django.shortcuts import render
from django.views.generic import View
import json
from .models import Student
from .utils import is_json
from .mixins import HttpResponseMixin,SerializeMixin
from .forms import StudentForm

# Create your views here.
class StudentCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            std = Student.objects.get(id=id)
        except Student.DoesNotExist:
            std = None
        return std
    
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({
                'msg':"Please provide valid json data"
            }),status=400)

        p_data = json.loads(data)
        id = p_data.get('id',None)

        if id is not None:
            std = self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({
                'msg':"No matched record found"
            }),status=400)
            json_data = self.serialize([std,])
            return self.render_to_http_response(json_data)
        
        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)
    
    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({
                'msg':"Please provide valid json data"
            }),status=400)

        p_data = json.loads(data)
        form = StudentForm(p_data)
        if form.is_valid():
            form.save()
            return self.render_to_http_response(json.dumps({'msg':"Resource created successfully"}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
        
    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({
                'msg':"Please provide valid json data"
            }),status=400)
        provided_data = json.loads(data)

        id = provided_data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({
                'msg':"To perform updation id is mandatory"
            }),status=400)
        std = self.get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({
                'msg':"No matched record found for the given id"
            }),status=404)
        original_data = {
            'name':std.name,
            'rollno':std.rollno,
            'marks':std.marks,
            'gf':std.gf,
            'bf':std.bf,
        }
        original_data.update(provided_data)
        form = StudentForm(original_data,instance=std)
        if form.is_valid():
            form.save()
            return self.render_to_http_response(json.dumps({'msg':"Resource updated successfully"}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400) 
    
    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({
                'msg':"Please provide valid json data"
            }),status=400)
        provided_data = json.loads(data)

        id = provided_data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({
                'msg':"To perform deletion id is mandatory"
            }),status=400)
        std = self.get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({
                'msg':"No matched record found for the given id"
            }),status=404)
        status,deleted_item = std.delete()
        if status == 1:
            return self.render_to_http_response(json.dumps({
                'msg':"Resource deleted successfully"
            }))
        json_data = json.dumps({'msg':"Unable to delete please try again"})
        return self.render_to_http_response(json_data,status=500)
        
                





            
