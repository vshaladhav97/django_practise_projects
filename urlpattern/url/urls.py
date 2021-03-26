from django.contrib import admin
from django.urls import path, re_path
from url import views
import uuid

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/', views.showdetails1, name='page1' ),
    path('page2/<int:my_id1>', views.urldetail, name='page2'),
    path('page3/<int:my_id2>', views.urlint, name='page3'),
    # path('profile/<slug:article_value>/', views.article),
    path('profile1/<uuid:uid>/', views.uids),
    # re_path(r'^\d+', views.repath, name='repath'),
    re_path(r'^(?P<number>\d+)', views.repath, name='repath'),
    # path('page2/<int:my_id1>', views.urldetail, name='page2'),
    path('abc/<str:my_id3>/', views.urldetails, name='abc'),
]
