from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Dpersonaldetails, name="Index"),
    path("<int:idx>/", views.personaldetails, name="Index"),
    path("ProjectDetails/<int:idx>", views.ProjectDetails, name="Project"),
    path("download_file/<int:idx>", views.download_file, name="download_file"),
    # path("upload/", views.upload_file, name="upload_file"),
    # path("Education", views.rparesumeindex),
    # path("Index", views.rparesumeindex),
]
