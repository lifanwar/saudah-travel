from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('about/', views.about, name='about'),
]
