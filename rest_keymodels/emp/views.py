from django.shortcuts import render
from .serializers import ContentSerializer
from .models import Topic, Content
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST'])
def topic_content_list(request, name):
    try:
        topic = Topic.objects.get(name=name)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        contents = Content.objects.filter(topic=topic)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data["topic"] = topic
        serializer = ContentSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)