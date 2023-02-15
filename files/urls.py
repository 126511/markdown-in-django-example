from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_file/", views.add_file, name="add_file"),
    path("view_file/<slug:id>/", views.view_file, name="view_file"),
    path("edit_file/<slug:id>/", views.edit_file, name="edit_file"),
]