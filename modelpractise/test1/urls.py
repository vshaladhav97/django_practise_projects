from test1.models import Students
from django.urls import path
from . import views


urlpatterns =[
    path('', views.studentinfo),
    path('filter/', views.studentlist, name='filter'),
    path('filter1/', views.student_teacher, name='filter1'),
    path('exclude/', views.student_list, name='exclude'),
    path('raw/', views.student_list1, name='raw'),
    path('pics/', views.details, name='pics'),
    path('data/', views.save_data_test, name='lists'),


] 