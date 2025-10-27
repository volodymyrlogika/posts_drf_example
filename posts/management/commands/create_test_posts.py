from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post
import random


class Command(BaseCommand):
    """
    Management команда для створення тестових постів
    Використання: python manage.py create_test_posts
    """
    help = 'Створює тестові пости для демонстрації динамічного підвантаження'

    def add_arguments(self, parser):
        # Додаємо аргумент для кількості постів
        parser.add_argument(
            '--count',
            type=int,
            default=50,
            help='Кількість постів для створення (за замовчуванням: 50)'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        # Перевіряємо, чи є користувачі в системі
        users = User.objects.all()
        if not users.exists():
            # Створюємо тестового користувача, якщо користувачів немає
            self.stdout.write(
                self.style.WARNING('Не знайдено користувачів. Створюю тестового користувача...')
            )
            user = User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
            users = [user]
        else:
            users = list(users)

        # Шаблони для генерації постів
        title_templates = [
            "Як налаштувати Django проект",
            "Основи роботи з Django REST Framework",
            "Створення API endpoints в DRF",
            "Робота з базами даних в Django",
            "Автентифікація в Django",
            "Тестування Django додатків",
            "Деплой Django на продакшн",
            "Оптимізація запитів в Django ORM",
            "Створення custom middleware",
            "Робота з файлами в Django",
            "Django vs Flask: порівняння",
            "Використання Django Admin",
            "Кешування в Django",
            "Безпека в Django додатках",
            "Django і фронтенд фреймворки",
            "Асинхронне програмування в Django",
            "Міграції баз даних",
            "Django signals і їх використання",
            "Створення власних template tags",
            "Інтернаціоналізація в Django"
        ]

        content_templates = [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.",
            "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet.",
            "Consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam.",
            "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident."
        ]

        # Створюємо пости
        posts_created = 0
        
        self.stdout.write(f'Створюю {count} тестових постів...')
        
        for i in range(count):
            # Випадково вибираємо шаблони
            title = f"{random.choice(title_templates)} #{i+1}"
            content = f"{random.choice(content_templates)} {random.choice(content_templates)}"
            author = random.choice(users)
            
            # Створюємо пост
            post = Post.objects.create(
                title=title,
                content=content,
                author=author,
                is_published=True
            )
            
            posts_created += 1
            
            # Показуємо прогрес кожні 10 постів
            if posts_created % 10 == 0:
                self.stdout.write(f'Створено {posts_created} постів...')

        self.stdout.write(
            self.style.SUCCESS(f'Успішно створено {posts_created} тестових постів!')
        )