from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Серіалізатор для моделі Post
    Перетворює об'єкти Post в JSON та навпаки
    """
    class Meta:
        model = Post
        fields = '__all__'

    