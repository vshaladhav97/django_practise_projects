from django.contrib import admin
from django.urls import path
from .views import ItemView

urlpatterns = [
    path('', ItemView.as_view()),
    # path('abc/', CustomerListView),
]