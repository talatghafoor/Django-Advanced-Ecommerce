from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showdata, name='showdata'),
]