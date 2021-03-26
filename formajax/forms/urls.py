from django.conf.urls import url, re_path
from forms import views

urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$',
        views.validate_username, name='validate_username'),
]
