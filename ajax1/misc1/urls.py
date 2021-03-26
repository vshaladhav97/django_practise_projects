from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin

from misc1.views import JoinFormView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^join/', JoinFormView.as_view()),
]