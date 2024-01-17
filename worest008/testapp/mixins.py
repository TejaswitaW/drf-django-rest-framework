from django.http import HttpResponse
from django.core.serializers import serialize
import json

class SerializeMixin:
    def serialize(self,qs):
        # converted qs to json data
        json_data = serialize('json',qs)
        # converted json data to dictionary
        p_data = json.loads(json_data)
        data_list = []
        for obj in p_data:
            emp_data = obj['fields']
            data_list.append(emp_data)
        json_data = json.dumps(data_list)
        return json_data
    
class HttpResponseMixin:
    def render_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)


              
        