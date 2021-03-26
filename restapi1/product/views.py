from django.shortcuts import render
# from django.http import HTTpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializer import ProductSerializer
from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.parsers import JSONParser
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def List(self, request):
        stu = Products.objects.all()
        serializer = ProductSerializer(stu, many=True)
        return Response(serializer._data)
    
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Products.objects.get(pk=id)
            serializer = ProductSerializer(stu)
            return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        id = pk
        stu = Products.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

