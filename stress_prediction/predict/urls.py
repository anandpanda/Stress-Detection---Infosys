# predict/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_recommend, name='predict_recommend'),
]
