from . import views
from django.urls import path
from .utils import unique_id

urlpatterns = [
    path("", views.faculty_view, name="faculty_view"),
    path(unique_id, views.add_manually, name="add_manually"),
]
