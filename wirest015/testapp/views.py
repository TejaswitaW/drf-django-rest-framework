from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import NameSerializer

class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors = ['RED','YELLOW','GREEN','BLUE']
        # this response class converts python dictionary to json automatically
        return Response({'msg':'Happy Birthday','colors':colors})
    def post(self,request,*args,**kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = f"Hello {name} ,Happy Birthday Dear!!"
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    def put(self,request,*args,**kwargs):
        return Response({'msg':'This is put method response'})
    def patch(self,request,*args,**kwargs):
        return Response({'msg':'This is patch method response'})
    def delete(self,request,*args,**kwargs):
        return Response({'msg':'This is delete method response'})
    # now all http methods are visible in browsable API page

class TestViewSet(ViewSet):
    def list(self,request):
        colors = ['RED','YELLOW','GREEN','BLUE']
        # this response class converts python dictionary to json automatically
        return Response({'msg':'Happy Birthday','colors':colors})
    def create(self,request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = f"Hello {name} ,Happy Birthday Dear!!"
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)
    def retrieve(self,request,pk=None):
        return Response({'msg':'This is retrieve method response'})
    def update(self,request,pk=None):
        return Response({'msg':'This is update method response'})
    def partial_update(self,request,pk=None):
        return Response({'msg':'This is partial update method response'})
    def destroy(self,request,pk=None):
        return Response({'msg':'This is destroy method response'})



