from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from .views import JoinFormView

urlpatterns =[
    path('abc/', views.showform),
    path('regis/', views.studentview, name='regis'),
    url(r'^join/', JoinFormView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)