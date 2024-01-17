from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from .permissions import IsReadOnly
from .authentications import CustomAuthentication,CustomAuthenticationKeyBased

from rest_framework_simplejwt.authentication import JWTAuthentication


class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [CustomAuthenticationKeyBased]
    permission_classes = [IsAuthenticated]



