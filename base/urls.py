from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.main,name='main'),
    path('calculate/', views.calculate,name='calc')
]