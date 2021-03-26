from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# from test1.models import *
# Create your views here.


def main_page(request):
    user = User.objects.create_user(username='john',
                                    email='jlennon@beatles.com',
                                    password='glass onion')
    user.save()


data = {
    "id": 60,
    "address_line_1": "little gibbs road",
    "address_line_2": "malabar hill",
    "city": "Mumbai",
    "country": "india",
    "pincode": "400006"
    "employees_address": [
        {
            "id": 41,
            "first_name": "ritin vijay",
            "last_name": "sharma",
            "username": "rikki",
            "date_of_birth": "1996-01-10",
            "gender": "M",
            "email_address": "riki@gmail.com",
            "contact_number": "7977361387",
            "deleted": True,
        }
    ]
}


data = {
    "id": 60, "address_line_1": "little gibbs", "address_line_2": "malabar hill", "city": "Mumbai", "country": "india", "pincode": "400006", "employees_address": {"id": 41,"first_name": "ritin vijay","last_name": "sharma","username": "rikki","date_of_birth": "1996-01-10","gender": "M","email_address": "riki@gmail.com","contact_number": "7977361387", "addressdetails":60 ,"deleted": True}}

from emp.serializers import AddressDetailsSerializer1, EmployeesSerializer1


data = {
    "id": 60, "address_line_1": "little gibbs", "address_line_2": "malabar hill", "city": "Mumbai", "country": "india", "pincode": "400006"}






    "<tr><td><button class='button2 update' onclick='changes(" + course.id + ")'><i class='fa fa-edit' style='font-size:15px'></i></button><button id = 'refresh' class='button3 delete' onclick='deleteCourse(" + course.addressdetails + ")'><i class='fa fa-trash' style='font-size:15px'></i></button><button class='button4' id='view' onclick='changes1(" + course.id + ")'><i class='far fa-eye' style='font-size:15px'></i></button></td><td class='editable' data-id=" + course.id + " data-type='first_name'>" +

                cours