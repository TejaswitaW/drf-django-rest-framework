from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from .pagination import CustomPageNumberPagination,CustomLimitOffsetPagination,CustomCursorPagePagiantion
'''
class EmployeeListView(ListAPIView):
    #queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # plain vanilla filtering
    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get('name')
        if name is not None:
            qs = qs.filter(ename__icontains=name)
        return qs
    
'''
class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ('ename',)
    ordering_fileds = ('eno','esal')



