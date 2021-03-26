from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from perm.decorator import access_permissions
from perm.constants import view_only_permission


class ProjectDetailView(APIView):

    @access_permissions(view_only_permission)
    def get(self, request, id):
        # code for handling get request
