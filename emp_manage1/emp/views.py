from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder
from rest_framework.views import APIView
from .serializers import EmployeesSerializer, DocumentSerializer, AddressDetailsSerializer, RoleSerializer
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .forms import SignUpForm
from rest_framework.response import Response
# Create your views here.


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/show/')
            else:
                messages.info(request, 'Username OR password is incorrect')
    else:
        fm = AuthenticationForm()
    return render(request, 'enroll/userlogin.html', {'form': fm})


class Management(APIView):

    def get(self, request):
        employee = Employees.objects.all()
        serializer = EmployeesSerializer(employee, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     # # addressdetails = get_object_or_404(AddressDetails, )
    #     serializer1 = EmployeesSerializer(data=request.data)
    #     # serializer2 = AddressDetailsSerializer(data=request.data)
    #     # serializer3 = RoleSerializer(data=request.data)
    #     # result = serializer1.data + serializer2.data + serializer3.data
    #     print(request.data)
    #     if serializer1.is_valid():
    #         serializer1.save()
    #         print(serializer1.data)
    #         return Response(serializer1.data,status=201)  # Successful post

    #     # elif serializer2.is_valid():
    #     #     serializer2.save()
    #     #     print(serializer2.data)
    #     #     return Response(serializer2.data, status=201) # Successful post

    #     # elif serializer3.is_valid():
    #     #     serializer3.save()
    #     #     print(serializer3.data)
    #     #     return Response(serializer3.data, status=201)
    #     return Response(serializer1.errors, status=400)  # Invalid data

    def post(self, request):
        json_data = request.data
        employees = {"first_name": json_data["first_name"], "last_name":json_data["last_name"], "username": json_data["username"],
                                "date_of_birth":json_data["date_of_birth"], "gender": json_data["gender"], "email_address":json_data["email_address"], "contact_number":json_data["contact_number"], "deleted": json_data["deleted"]}

        address_data = request.data
        address_details = {

            "address_line_1": address_data["address_line_1"],
            "address_line_2": address_data["address_line_2"],
            "city": address_data["city"],
            "country": address_data["country"],
            "pincode": address_data["pincode"]
        }

        address = AddressDetailsSerializer(data=address_details)
        print(address.is_valid())
        
        employee = EmployeesSerializer(data=employees, instance=address)
        print(employee.is_valid())
        if employee.is_valid():
            employee.save()
            return Response(status=201)
        return Response(status=400)
    
    def put(self, request, pk)



def clients(request):
    return render(request, "enroll/emplist.html")


def clients1(request):
    return render(request, "enroll/addemp.html")


def clients2(request):
    return render(request, "enroll/showemp.html")
