from django.shortcuts import render
# from django.http import HTTpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Products, Post
from .serializer import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status



@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        obj = Products.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        obj = Products.objects.get(id=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_Found)

    if request.method == 'GET':
        serializer = ProductSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        serializer = ProductSerializer(obj)
        return Response(serializer.data)


class Product_list1(APIView):
    def get(self, request):
        obj = Products.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_)

# @csrf_exempt
def post_list2(request):
    if request.method == 'GET':
        post = Products.objects.all()
        serializer = ProductSerializer(post, many =True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def displaydata(request):
    callapi = request.get('http://127.0.0.1:8000/product/')
    result = callapi.json()
    return render(request, 'enroll/index.html', {'ProductSerializer':result})

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        queryset = Profile.objects.all()
        return Response({'profiles': queryset})
    
    
def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post=Post()
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()
            return render(request, 'enroll/test.html')  

    else:
            return render(request,'enroll/test.html')