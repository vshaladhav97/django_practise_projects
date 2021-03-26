from django.contrib import admin
from django.urls import path
# from .import views
from .views import product_list, product_detail, Product_list1, post_list2, displaydata, createpost
urlpatterns = [
    path('product/', product_list),
    path('product/<int:pk>', product_detail),
    path('classproduct/', Product_list1.as_view()),
    path('parser/', post_list2),
    path('a/', displaydata),
    path('', createpost),
    

]
