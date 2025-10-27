#!/usr/bin/env python
"""
Скрипт для додавання 30 тестових постів в БД за допомогою Django ORM
Використання: python add_posts.py
"""

import os
import sys
import django

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'posts_drf_example.settings')
django.setup()

# Імпортуємо моделі після налаштування Django
from django.contrib.auth.models import User
from posts.models import Post


def create_test_posts():
    """
    Створює 30 тестових постів
    """
    # Перевіряємо, чи є користувачі
    if not User.objects.exists():
        print("Створюю тестового користувача...")
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    else:
        user = User.objects.first()
    
    # Список заголовків для постів
    titles = [
        "Вступ до Django",
        "Створення моделей",
        "Django REST Framework",
        "Робота з базами даних",
        "Система аутентифікації",
        "Створення API",
        "Пагінація в DRF",
        "Серіалізатори",
        "ViewSets та Routers",
        "Фільтрація та пошук",
        "Права доступу",
        "Тестування API",
        "Документація API",
        "Деплой на продакшн",
        "Кешування в Django",
        "Оптимізація запитів",
        "Middleware в Django",
        "Сигнали Django",
        "Async Views",
        "Webhooks",
        "Інтеграція з React",
        "GraphQL з Django",
        "Мікросервіси",
        "Docker з Django",
        "CI/CD пайплайни",
        "Моніторинг",
        "Логування",
        "Безпека API",
        "Версіонування API",
        "Performance туning"
    ]
    
    # Список змісту для постів
    contents = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.",
        
        "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt.",
        
        "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.",
        
        "Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus."
    ]
    
    print("Створюю 30 тестових постів...")
    
    # Видаляємо існуючі пости для чистого тесту
    Post.objects.all().delete()
    print("Видалив існуючі пости")
    
    # Створюємо 30 постів
    created_posts = []
    for i in range(30):
        post = Post.objects.create(
            title=titles[i],
            content=contents[i % len(contents)],  # Циклічно використовуємо контент
            author=user,
            is_published=True
        )
        created_posts.append(post)
        print(f"Створено пост {i+1}: {post.title}")
    
    print(f"\n✅ Успішно створено {len(created_posts)} постів!")
    print(f"Автор всіх постів: {user.username}")
    print("\nПерші 5 постів:")
    for post in created_posts[:5]:
        print(f"- {post.title}")


if __name__ == "__main__":
    try:
        create_test_posts()
    except Exception as e:
        print(f"❌ Помилка: {e}")
        sys.exit(1)