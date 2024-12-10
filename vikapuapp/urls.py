from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my home'),
    path('customdesigns/', views.customdesigns, name='custom designs'),
    path('newdesigns/', views.newdesigns, name='new designs'),
    path('plainbaskets/', views.plainbaskets, name='plain basket')
]



