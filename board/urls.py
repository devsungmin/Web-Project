from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post_create/', views.post_create, name="post_create"),
    path('post_detail/<int:id>/', views.post_detail, name="post_detail"),
    path('post_update/<int:id>/', views.post_update, name="post_update"),
    path('post_delete/<int:id>/', views.post_delete, name="post_delete"),
]