from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from crud.serializers import CourseSerializer
# from .forms import VideoForm



def client(request):
    return render(request, "enroll/rest_client.html")


@api_view(['GET', 'POST'])
def list_courses(request):
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    else:  # Post
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  # Invalid data


@api_view(['GET', 'DELETE', 'PUT'])
def course_details(request, code):
    try:
        course = Course.objects.get(code=code)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT':    # Update
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()    # Update table in DB
            return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=204)


class Management(APIView):
    # def get_object(self, code):
    #     try:
    #         return Course.objects.get(code=code)
    #     except Course.DoesNotExist:
    #         raise Http404

    def get(self, request):
        courses = Course.objects.all()
        # course = Course.objects.get(code=code)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    # def get(self, request, code):
    #     Course = self.get_object(code = code)
    #     serializer = CourseSerializer(Course, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  # Invalid data

    # def put(self, request, code):
    #     Course = self.get_object(code=code)
    #     serializer = CourseSerializer(Course, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, code):
    #     course = Course.objects.get(code=code)
    #     serializer = CourseSerializer(course, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()    # Update table in DB
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)  # Bad request

    # def delete(self, request, code):
    #     course = Course.objects.get(code=code)
    #     course.delete()s
    #     return Response(status=204)
    # def delete(self, request, code):
    #     Course = self.get_object(code=code)
    #     Course.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class ManagementUpdate(APIView):
    
    def get_object(self, code):
        try:
            return Course.objects.get(code=code)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,code):
        course = self.get_object(code)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, code):
        course = self.get_object(code)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()    # Update table in DB
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Bad request
    
    def delete(self, request, code):
        course = self.get_object(code=code)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def clients(request):
    return render(request, "enroll/rest_client1.html")
