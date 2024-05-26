from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.fa_list, name='fa_list'),
    path('<int:pk>/', views.fa_detail, name='fa_detail')
]
