from django.contrib import admin
from django.urls import path, include
from dbapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("medicines/", include("dbapp.urls")),
    path("", views.go_to_medicine_page, name="index"),
]
