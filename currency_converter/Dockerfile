# Используем официальный образ Python
FROM python:3.11

# Устанавливаем зависимости
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в рабочую директорию
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED 1

# Применяем миграции и создаем суперпользователя
RUN python manage.py migrate
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell || true

# Запуск приложения
CMD ["gunicorn", "currency_converter.wsgi:application", "--bind", "0.0.0.0:8000"]
