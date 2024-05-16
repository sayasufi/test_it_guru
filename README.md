# Currency Converter

Currency Converter — это веб-приложение на основе Django, которое позволяет пользователям конвертировать валюты с использованием актуальных курсов валют от Центрального банка России.

## Функциональность

- Конвертация валют с использованием актуальных курсов
- Поддержка различных валют
- Удобный интерфейс с темной темой
- Поддержка поиска по валютам в выпадающем списке

## Требования

- Python 3.11
- Django
- Docker (для контейнеризации)
- Docker Compose (для управления контейнерами)

## Установка и запуск без Docker

### Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/ваш-репозиторий/currency_converter.git
cd currency_converter
```

### Шаг 2: Создание виртуального окружения
```bash
python3 -m venv env
source env/bin/activate  # для Windows используйте `env\Scripts\activate`
```

### Шаг 3: Установка зависимостей
```bash
pip install -r requirements.txt
```

### Шаг 4: Применение миграций
```bash
python manage.py migrate
```

### Шаг 5: Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Шаг 6: Запуск сервера разработки
```bash
python manage.py runserver
```
Приложение будет доступно по адресу http://127.0.0.1:8000.

## Установка и запуск с использованием Docker

### Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/ваш-репозиторий/currency_converter.git
cd currency_converter
```

### Шаг 2: Создание файла .env
Создайте файл .env в корне проекта со следующим содержимым:
```env
DEBUG=1
SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DATABASE_URL=postgres://postgres:postgres@db:5432/currency_converter
```

### Шаг 3: Сборка контейнеров
```bash
docker-compose build
```

### Шаг 4: Запуск контейнеров
```bash
docker-compose up
```

Приложение будет доступно по адресу http://localhost:8000