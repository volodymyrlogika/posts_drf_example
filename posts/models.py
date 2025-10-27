from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Вміст")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

    def __str__(self):
        return f"{self.title} - {self.author.username}"

