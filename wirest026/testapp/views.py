from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from .pagination import CustomPageNumberPagination,CustomLimitOffsetPagination,CustomCursorPagePagiantion

# class EmployeeListView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     pagination_class = CustomPageNumberPagination

# class EmployeeListView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     pagination_class = CustomLimitOffsetPagination

class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomCursorPagePagiantion




