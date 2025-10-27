from django.urls import path
from . import views

# Простір імен для додатку posts
app_name = 'posts'

urlpatterns = [
    # Головна сторінка зі списком постів
    path('', views.posts_list_view, name='posts_list'),
    
    # API endpoints для роботи з постами
    path('api/posts/', views.PostListAPIView.as_view(), name='posts_api_list'),
]