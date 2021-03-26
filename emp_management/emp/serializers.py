from rest_framework import serializers
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder


class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    addressdetails = AddressDetailsSerializer(read_only=True)
    roles = RoleSerializer(read_only=True)

    # def create(self, validated_data):
    #     temp_bok_details = validated_data.pop('addressdetails')
    #     new_book = Employees.objects.create(**validated_data)
    #     for i in temp_bok_details:
    #         AddressDetails.objects.create(**i,bok=new_book)
    #     return new_book
    
    class Meta:
        model = Employees
        fields = ('id', 'first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'addressdetails', 'roles', 'deleted')
        # fields = '__all__'
    
    # def post(self, validated_data):
    #     return Employees.objects.create(**validated_data)    
    
    # def update(self, instance, validated_data):
    #     instance.__dict__.update(**validated_data)
    #     instance.save()
    #     return instance
    
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'
