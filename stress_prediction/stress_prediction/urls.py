from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),  # Homepage routes
    path("auth/", include("authentication.urls")),  # Authentication routes
    path("dataentry/", include("dataentry.urls")),  # Data entry routes
    path("predict/", include("predict.urls")),  # Prediction routes
]
