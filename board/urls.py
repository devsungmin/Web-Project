from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post_create/', views.post_create, name="post_create"),
    path('post_detail/<int:id>/', views.post_detail, name="post_detail"),
    path('post_update/<int:id>/', views.post_update, name="post_update"),
    path('post_delete/<int:id>/', views.post_delete, name="post_delete"),
    path('comment_create/<int:id>', views.comment_create, name="comment_create"),
    path('comment_update/<int:id>/', views.comment_update, name="comment_update"),
    path('comment_delete/<int:id>/', views.comment_delete, name="comment_delete"),
]