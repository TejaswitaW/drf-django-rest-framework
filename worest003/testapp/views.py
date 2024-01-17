from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
import json
from .mixins import HttpResponseMixin

class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data = {'msg':"This is GET method"}
        json_data = json.dumps(data)
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        data = {'msg':"This is POST method"}
        json_data = json.dumps(data)
        return self.render_to_http_response(json_data)
    def put(self,request,*args,**kwargs):
        data = {'msg':"This is PUT method"}
        json_data = json.dumps(data)
        return self.render_to_http_response(json_data)
    def delete(self,request,*args,**kwargs):
        data = {'msg':"This is DELETE method"}
        json_data = json.dumps(data)
        return self.render_to_http_response(json_data)





