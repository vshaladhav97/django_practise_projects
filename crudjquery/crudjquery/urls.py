"""crudjquery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_courses/',  views.list_courses),
    re_path('rest_courses/(?P<code>\w+)/$', views.course_details),
    path('rest_client/', views.client),
    path('classproduct/', views.Management.as_view()),
    path('rest_client1/', views.clients),
    re_path('classproduct/(?P<code>\w+)/$', views.ManagementUpdate.as_view()),

]
