from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Items
from .serializers import ItemSerializer, ItemsSchema
import time
import requests
from rest_framework import status
from rest_framework import generics
# Create your views here.



# class CustomerListView(generics.ListAPIView):
#     queryset = Items.objects.all()
#     serializer_class = ItemsSchema
    
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = ItemsSchema(queryset, many=True)
#         return Response(serializer.data)

class ItemView(APIView):
    
    
    
    def get(self, request):
        
        item = Items.objects.filter(id = 1)
    

        serializers = ItemSerializer(item, many=True)

        print(serializers.data)
        
        return Response(serializers.data)
    
    def post(self, request):

        # json_data = request.data
        # item_data = {"status": json_data["status"], "items": json_data["items"]}
        # print(json_data)
        serializer = ItemSerializer(data=request.data)
        # item = ItemsSchema(data=item_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # print(item.is_valid())
        # if item.is_valid():
        #     item.save()
        #     return Response(status=200)
        # else:
        #     return Response(status=400)


