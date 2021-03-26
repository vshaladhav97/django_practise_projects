from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import sign_up, Management, client, client1, user_login, logoutUser


urlpatterns = [
    
    path('signup/', sign_up, name='signup'),
    path('', user_login, name='login'),
    path('logout/', logoutUser, name="logout"),
    path('rest_client1/classproduct/', Management.as_view()),
    path('show/', login_required(client1), name='show'),
    path('show/classproduct/', login_required(Management.as_view())),
    path('loan/', client),
    path('loan/classproduct/', Management.as_view()),
    
    
    
]