from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import EmployeeForm, DocumentsForm, EmployeeStatusForm, AddressDetailsForm, RolesForm, DocumentVersionsForms, EmployeeDocumentForm, DocumentFolderForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Employees, Documents, AddressDetails, EmployeeStatus, Roles, DocumentVersions, EmployeeDocument, DocumentFolder
# from django.contrib.auth.models import Group
# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from django.contrib import messages
from rest_framework.response import Response
# from .serializers import PostSerializer, studentSerializer, CourseSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
# from django.contrib.auth.decorators import login_required
# from .decorators import unauthenticated_user
# Create your views here.
# @unauthenticated_user
# def registerPage(request):

#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')

#             group = Group.objects.get(name='staffs')
#             user.groups.add(group)

#             messages.success(request, 'Account was created for ' + username)

#             return redirect('login')

#     context = {'form': form}
#     return render(request, 'enroll/register.html', context)

# @unauthenticated_user
# def loginPage(request):

# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		password =request.POST.get('password')

# 		user = authenticate(request, username=username, password=password)

# 		if user is not None:
# 			login(request, user)
# 			return redirect('/show')
# 		else:
# 			messages.info(request, 'Username OR password is incorrect')

# 	context = {}
# 	return render(request, 'enroll/login.html', context)


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


def user_profile(request):
    return render(request, 'enroll/profile.html')


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:

                form.save()
                return redirect('/show')
            except:
                return "invalid data"
    else:
        form = EmployeeForm()
    return render(request, 'enroll/index.html', {'form': form})


def show(request):
    employees = Employees.objects.all()
    return render(request, "enroll/show.html", {"employees": employees})


def edit(request, id):
    if request.method == 'POST':
        pi = Employees.objects.get(id=id)
        form = EmployeeForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        pi = Employees.objects.get(id=id)
        form = EmployeeForm(request.POST, instance=pi)
    return render(request, "enroll/edit.html", {'form': form})

# def update(request, id):
#     employees = Employees.objects.get(id=id)
#     form = EmployeeForm(request.POST, instance=employees)
#     if form.is_valid():
#         form.save()
#         return redirect("/show")
#     return render(request, "enroll/edit.html", {'employees': employees})


def delete(request, id):
    employees = Employees.objects.get(id=id)
    employees.delete()
    return redirect("/show")


def emp1(request):
    if request.method == 'POST':
        form = EmployeeStatusForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                return "invalid data"
    else:
        form = EmployeeStatusForm()
    return render(request, 'enroll/index1.html', {'form': form})


def createpost(request):
    if request.method == 'POST':
        #     if request.POST.get('title') and request.POST.get('content'):
        #         post = Post()
        #         post.title = request.POST.get('title')
        #         post.content = request.POST.get('content')
        #         post.save()
        #         return render(request, 'enroll/test.html')
        # id = 1
        # data = request.POST
        # ret = Post.objects.create(
        #     user=id, title=data.title, content=data.content)
        # if ret:
        #     return HttpResponse("your data is submitted")
        # else:
        #     return HttpResponse("your data is not submitted")

        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            # print(serializers.data)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_)

    elif request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        pi = serializer.data
        context = {'pi': pi}
        return render(request, 'enroll/test.html', context)

    else:
        return render(request, 'enroll/test.html')


# def createpost(request):
#     if request.method == 'POST':
#         if request.POST.get('title') and request.POST.get('content'):
#             post=Post()
#             post.title= request.POST.get('title')
#             post.content= request.POST.get('content')
#             post.save()
#             return render(request, 'enroll/test.html')
#     else:
#         return render(request, 'enroll/test.html')

# def post(self, *args, **kwargs):
#         if self.request.is_ajax and self.request.method == "POST":
#             form = self.form_class(self.request.POST)
#             if form.is_valid():
#                 instance = form.save()
#                 ser_instance = serializers.serialize('json', [ instance, ])
#                 # send to client side.
#                 return JsonResponse({"instance": ser_instance}, status=200)
#             else:
#                 return JsonResponse({"error": form.errors}, status=400)

#         return JsonResponse({"error": ""}, status=400)

# class FriendView(View):
#     form_class = FriendForm
# template_name = "index.html"

#     def get(self, *args, **kwargs):
#         form = self.form_class()
#         friends = Friend.objects.all()
#         return render(self.request, self.template_name,
#                         {"form": form, "friends": friends})

#     def post(self, *args, **kwargs):
#         if self.request.is_ajax and self.request.method == "POST":
#             form = self.form_class(self.request.POST)
#             if form.is_valid():
#                 instance = form.save()
#                 ser_instance = serializers.serialize('json', [instance, ])
#                 # send to client side.
#                 return JsonResponse({"instance": ser_instance}, status=200)
#             else:
#                 return JsonResponse({"error": form.errors}, status=400)

#         return JsonResponse({"error": ""}, status=400)
# @login_required(login_url="login/")
# def home(request):
#     return render(request,"home.html")

# class PoliceViewset(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     # print(queryset)
#     serializer_class = PostSerializer
#     print(serializer_class)


# class Get_students_List(APIView):
#     def get(self, request):
#         students = Students.objects.all()
#         serialized = studentSerializer(students, many=True)
#         # print(serialized.data)
#         return Response(serialized.data)

#     def post(self, request):
#         # serializer = studentSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     print(serializer.data)
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_)
#         serializer = studentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response(serializer.data, status=201)  # Successful post

#         return Response(serializer.errors, status=400)


# def homepage(request):
#     return render(request, 'enroll/indexss.html')


# # def homepage1(request):
# #     return render(request, 'enroll/abc.html')


# def client(request):
#     return render(request, "enroll/rest_client.html")


# @api_view(['GET', 'POST'])
# def list_courses(request):
#     if request.method == "GET":
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)
#     else:  # Post
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)  # Successful post

#         return Response(serializer.errors, status=400)  # Invalid data


# @api_view(['GET', 'DELETE', 'PUT'])
# def course_details(request, code):
#     try:
#         course = Course.objects.get(code=code)
#     except:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)
#     elif request.method == 'PUT':    # Update
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()    # Update table in DB
#             return Response(serializer.data)

#         return Response(serializer.errors, status=400)  # Bad request
#     elif request.method == 'DELETE':
#         course.delete()
#         return Response(status=204)
