from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("add_manually_post", views.add_manually_post, name="add_manually_post"),
    path("submitted", views.submitted, name="submitted"),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
 
]
