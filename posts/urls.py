from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:id>/edit/', views.update_post, name='update_post'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
]