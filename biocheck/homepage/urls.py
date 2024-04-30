from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about')
]
