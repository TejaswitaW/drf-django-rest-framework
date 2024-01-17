from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from .permissions import IsReadOnly


class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsReadOnly]



