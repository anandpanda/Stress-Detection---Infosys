from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_data_form, name="user_data_form"),
]
