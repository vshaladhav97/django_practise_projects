"""employee_management URL Configuration

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
from django.conf.urls import url
from employee.views import user_profile, show, delete, emp, emp1, edit, sign_up, user_login, createpost

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/', registerPage, name="register"),
    # path('login/', loginPage, name="login"),
    path('signup/', sign_up, name='signup'),
    path('login/', user_login, name='login'),
    path('profile/', user_profile, name='profile'),
    path('create/', emp),
    path('show/', show),
    path('edit/<int:id>', edit),
    path('delete/<int:id>', delete),
    path('eds/', emp1),
    path('post/', createpost, name='post'),
    # url(r'PoliceAssurance', PoliceViewset.as_view(), name='PoliceAssurance'),
    # url(r'^home$', homepage),
    # # url(r'^insert$', homepage1, name='insert'),
    # url(r'^studentsapi$', Get_students_List.as_view()),
    # path('rest_courses/',  list_courses),
    # re_path('rest_courses/(?P<code>\w+)/$', course_details),
    # path('rest_client/', client),
]
