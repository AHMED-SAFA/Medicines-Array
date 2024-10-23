from django.urls import path
from dbapp import views

urlpatterns = [
    path("data/", views.show_medicine_page, name="data"),
]
