from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createPost, name='create-post'),
    path('add_category/', views.addCategory, name='add-category'),
]