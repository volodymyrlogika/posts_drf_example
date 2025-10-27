from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'likes_count', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
    readonly_fields = ['likes_count', 'created_at', 'updated_at']
    filter_horizontal = ['likes']  # Зручний інтерфейс для ManyToManyField
