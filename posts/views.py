from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer


class PostPagination(PageNumberPagination):
    """
    Клас для пагінації постів (розбиття на сторінки)
    Визначає скільки постів показувати на одній сторінці
    """
    page_size = 10  # Кількість постів на сторінці
    page_size_query_param = 'page_size'  # Параметр для зміни розміру сторінки
    max_page_size = 50  # Максимальний розмір сторінки


class PostListAPIView(generics.ListAPIView):
    """
    API view для отримання списку постів з пагінацією
    GET /api/posts/ - повертає список постів
    GET /api/posts/?page=2 - повертає другу сторінку постів
    """
    queryset = Post.objects.filter(is_published=True)  # Тільки опубліковані пости
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        """
        Фільтрація постів (можна додати пошук, сортування тощо)
        """
        queryset = super().get_queryset()
        
        
        return queryset


def posts_list_view(request):
    """
    Звичайний Django view для відображення сторінки з постами
    Тут відображається HTML шаблон з JavaScript для динамічного підвантаження
    """
    context = {
        'page_title': 'Список постів',
        'api_url': '/api/posts/',  # URL для API запитів
    }
    return render(request, 'posts/posts_list.html', context)
