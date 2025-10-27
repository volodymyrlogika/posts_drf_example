# 📝 Django + DRF Приклад Динамічного Підвантаження Постів з Лайками

Мінімалістичний приклад роботи з динамічним підвантаженням постів та системою лайків за допомогою Django REST Framework та JavaScript.

## 🎯 Що демонструє цей проект

- Створення API endpoints з Django REST Framework
- Пагінацію з DRF (по 10 постів на сторінку)
- Динамічне підвантаження контенту за допомогою JavaScript
- Систему лайків з ManyToManyField
- Роботу з Fetch API для AJAX запитів
- Автентифікацію користувачів

## 📁 Структура проекту

```
posts_drf_example/
├── posts/                  # Додаток для роботи з постами
│   ├── models.py           # Модель Post з системою лайків
│   ├── views.py            # API views та звичайні views
│   ├── serializers.py      # DRF сериалізатори
│   ├── admin.py            # Налаштування Django Admin
│   └── urls.py             # URL маршрути
├── accounts/               # Додаток для автентифікації
├── templates/
│   ├── base.html           # Базовий шаблон з Bootstrap
│   └── posts/
│       └── posts_list.html # Головна сторінка з JavaScript
├── static/css/
│   └── style.css           # Стилі для динамічного підвантаження
├── add_posts.py            # Скрипт для додавання тестових постів
└── add_posts_simple.py     # Простий скрипт для створення постів
```

## 🚀 Швидкий старт

### 1. Підготовка середовища

```bash
# Активуйте віртуальне середовище
.venv\Scripts\activate   # Windows
# або
source .venv/bin/activate   # Linux/macOS

# Встановіть залежності
pip install -r requirements.txt
```

### 2. Налаштування бази даних

```bash
# Створіть та застосуйте міграції
python manage.py makemigrations
python manage.py migrate

# Створіть суперкористувача
python manage.py createsuperuser
```

### 3. Додайте тестові дані

Детальний скрипт з 30 різними постами**
```bash
python add_posts.py
```

### 4. Запустіть сервер

```bash
python manage.py runserver
```

Перейдіть на http://127.0.0.1:8000/ щоб побачити роботу динамічного підвантаження.

## 🔧 API Endpoints

- `GET /api/posts/` - Список постів з пагінацією
- `GET /api/posts/?page=2` - Друга сторінка постів
- `POST /api/posts/{id}/toggle-like/` - Додати/прибрати лайк (потрібна авторизація)
- `GET /admin/` - Django Admin панель

## 💻 Як працює динамічне підвантаження

1. **Початкове завантаження**: JavaScript робить запит до `/api/posts/` і отримує перші 10 постів
2. **Кнопка "Завантажити ще"**: При натисканні робиться запит на наступну сторінку
3. **Додавання контенту**: Нові пости додаються до DOM без перезавантаження сторінки
4. **Система лайків**: Кожен пост має кнопку лайку з Bootstrap іконками

## ❤️ Система лайків

- **ManyToManyField**: Зв'язок між постами та користувачами через проміжну таблицю
- **Toggle функціонал**: Один клік додає лайк, другий - прибирає
- **Real-time оновлення**: Кількість лайків оновлюється без перезавантаження

## 📚 Ключові компоненти

### Models (posts/models.py)
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    # Система лайків через ManyToManyField
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    @property
    def likes_count(self):
        return self.likes.count()
```

### API Views (posts/views.py)
```python
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    pagination_class = PostPagination  # 10 постів на сторінку

@api_view(['POST'])
def toggle_like(request, post_id):
    if not request.user.is_authenticated:
        return Response({'error': 'Потрібна авторизація'}, status=401)
    
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    
    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True
    
    return Response({'liked': liked, 'likes_count': post.likes_count})
```

### JavaScript для лайків
```javascript
async function toggleLike(postId) {
    const response = await fetch(`/api/posts/${postId}/toggle-like/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    });
    
    const data = await response.json();
    document.querySelector(`[data-post-id="${postId}"] .likes-count`)
            .textContent = data.likes_count;
}
```

