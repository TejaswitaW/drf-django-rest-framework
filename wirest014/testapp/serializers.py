from rest_framework import serializers
from .models import Employee

# implement own validator
def multiples_of_1000(value):
    if value%1000 != 0:
        raise serializers.ValidationError("Employee salary should be multiple of 1000")

class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiples_of_1000])
    class Meta:
        model = Employee
        fields = '__all__'