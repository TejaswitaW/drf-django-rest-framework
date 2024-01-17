from rest_framework import serializers
from .models import Employee

# implement own validator
def multiples_of_1000(value):
    if value%1000 != 0:
        raise serializers.ValidationError("Employee salary should be multiple of 1000")

class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField(validators=[multiples_of_1000])
    eaddr = serializers.CharField(max_length=100)

    # field level validation
    def validate_esal(self,value):
        if value < 5000:
            raise serializers.ValidationError("Employee Salary should be minimum 5000")
        return value
    
    # object level validation
    def validate(self,data):
        ename = data.get('ename')
        esal = data.get('esal')
        if ename.lower() == "kartiki":
            if esal < 500000:
                raise serializers.ValidationError("Kartiki salary should be minimum 500000")
        return data
    

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print("Inside update before")
        instance.eno = validated_data.get('eno',instance.eno)
        instance.ename = validated_data.get('ename',instance.ename)
        instance.esal = validated_data.get('esal',instance.esal)
        instance.eaddr = validated_data.get('eaddr',instance.eaddr)
        instance.save()
        print("Inside update after")
        print("instance: ",instance,instance.eno,instance.ename,instance.esal,instance.eaddr)
        return instance