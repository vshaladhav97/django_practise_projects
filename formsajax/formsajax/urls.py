"""formsajax URL Configuration

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
from django.urls import path
from form import views as app1
# from app_1 import views as app1
from form1 import views as app2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.contactPage),  # FBV
    path('ajax/contact', app1.postContact, name='contact_submit'),
    path('', app1.ContactAjax.as_view(), name = 'contact_submit'), #cbv
    #app_2
    path('user', app2.userPanel),
    path('ajax/get_user_info', app2.getUserInfo, name = 'get_user_info'),
]
