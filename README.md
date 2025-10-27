# 📝 Django + DRF Приклад Динамічного Підвантаження Постів

Мінімалістичний приклад роботи з динамічним підвантаженням постів за допомогою Django REST Framework та JavaScript.

## 🎯 Що демонструє цей проект

- Створення API endpoints з Django REST Framework
- Пагінацію з DRF (по 10 постів на сторінку)
- Динамічне підвантаження контенту за допомогою JavaScript
- Роботу з Fetch API для AJAX запитів

## 📁 Структура проекту

```
posts_drf_example/
├── posts/                  # Додаток для роботи з постами
│   ├── models.py           # Модель Post
│   ├── views.py            # API views та звичайні views
│   ├── serializers.py      # DRF сериалізатори
│   ├── admin.py            # Налаштування Django Admin
│   └── urls.py             # URL маршрути
├── templates/
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
```

### 3. Додайте тестові дані

**Варіант 1: Детальний скрипт з 30 різними постами**
```bash
python add_posts.py
```

**Варіант 2: Простий скрипт**
```bash
python add_posts_simple.py
```

### 4. Запустіть сервер

```bash
python manage.py runserver
```

Перейдіть на http://127.0.0.1:8000/ щоб побачити роботу динамічного підвантаження.

## 🔧 API Endpoints

- `GET /api/posts/` - Список постів з пагінацією
- `GET /api/posts/?page=2` - Друга сторінка постів
- `GET /admin/` - Django Admin панель

## 💻 Як працює динамічне підвантаження

1. **Початкове завантаження**: JavaScript робить запит до `/api/posts/` і отримує перші 10 постів
2. **Кнопка "Завантажити ще"**: При натисканні робиться запит на наступну сторінку
3. **Додавання контенту**: Нові пости додаються до DOM без перезавантаження сторінки
4. **Індикатори стану**: Показуються спінери завантаження та повідомлення про помилки

## 📚 Ключові компоненти

### Models (posts/models.py)
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
```

### API Views (posts/views.py)
```python
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    pagination_class = PostPagination  # 10 постів на сторінку
```

### JavaScript клас для підвантаження
```javascript
class PostsLoader {
    constructor(apiUrl) {
        this.apiUrl = apiUrl;
        this.currentPage = 1;
        this.loadPosts();  // Початкове завантаження
    }
    
    async loadPosts() {
        const response = await fetch(`${this.apiUrl}?page=${this.currentPage}`);
        const data = await response.json();
        this.renderPosts(data.results);
    }
}
```

## 🎓 Навчальні цілі

Цей приклад демонструє учням:

1. **Backend (Django + DRF)**:
   - Створення REST API
   - Пагінацію даних
   - Серіалізацію об'єктів

2. **Frontend (JavaScript)**:
   - Асинхронні запити з Fetch API
   - Динамічне створення DOM елементів
   - Обробку станів завантаження та помилок

3. **Інтеграцію**:
   - Взаємодію між frontend та backend
   - JSON формат даних
   - RESTful підходи

## 🛠 Додаткові можливості

- Пошук постів (можна розширити в `get_queryset`)
- Фільтрацію по авторах
- Сортування по різним полям
- Infinite scroll замість кнопки

## 👥 Користувачі за замовчуванням

Скрипт `add_posts.py` створює:
- **Адміністратор**: `admin` / `admin123`
- **Тестовий користувач**: `testuser` / `testpass123`