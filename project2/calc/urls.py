# from calc.views import Myview

from django.contrib import admin
from django.urls import path
from calc import views
from django.views.generic import TemplateView
# from calc.views import Ex2View
# app_name = 'website'
urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("cl/", views.Myview.as_view(), name='cl'),
    # path("cl/", views.Myview.as_view(name='ritin'), name='cl'),
    path("subcl/", views.Mychild.as_view(), name='subcl'),
    # extra_context Attribute from ContentMixin - keyword argument for as_view()
    # path('ex1', TemplateView.as_view(template_name="ex1.html",
    #                                 extra_context={'title': 'Custom Title'})),
    # path('ex2/', Ex2View.as_view(), name='ex2'),
#     path('homes/', views.TemplateView.as_view(template_name='homes.html'), name='home'),
#     path('homes1/', views.TemplateView.as_view(template_name='homes.html'), name='home1')
    # path('homes/', views.HomeTemplateView.as_view(extra_context = {'course':'python'}), name='homes'),
    # path('index1/', views.RedirectView.as_view(url = '/'), name='index1'),
    path('site/', views.HomeRedirectView.as_view(), name='site'),
]
