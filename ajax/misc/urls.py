from django.conf.urls import url, re_path
from misc import views

urlpatterns = [
    # url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    # # url('', views.SignUpView.as_view(), name='signup'),
    # url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^$', views.index, name='index'),  # index view at /
    url(r'^likepost/$', views.likePost, name='likepost'),
]
