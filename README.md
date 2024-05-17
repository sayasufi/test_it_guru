# Currency Converter

Currency Converter — это веб-приложение на основе Django, которое позволяет пользователям конвертировать валюты с использованием актуальных курсов валют от Центрального банка России.

## Функциональность

- Конвертация валют с использованием актуальных курсов
- Поддержка различных валют
- Удобный интерфейс с темной темой
- Поддержка поиска по валютам в выпадающем списке
- Асинхронная обработка запросов с использованием AJAX для обновления результатов без перезагрузки страницы

### Конвертация валют
Для конвертации валют перейдите по адресу:

```bash
http://localhost:8000/converter/
```
На этой странице вы можете выбрать исходную и целевую валюты, ввести сумму и нажать "Конвертировать", чтобы получить результат.

### API для конвертации валют
Приложение также предоставляет API для конвертации валют. Пример запроса:

```vbnet
GET /api/rates/?from=USD&to=RUB&value=1
```
Ответ:
```json
{
    "result": 62.16
}
```
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

### Шаг 4: Создание файла .env
Создайте файл .env в корне проекта со следующим содержимым:
```env
DEBUG=1
SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

### Шаг 5: Применение миграций
```bash
python manage.py migrate
```

### Шаг 6: Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Шаг 7: Запуск сервера разработки
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
```

### Шаг 3: Настройка docker-compose.yml
```env
    environment:
      - USE_DOCKER=true
      - DB_NAME=your_db_name
      - DB_USER=your_db_user
      - DB_PASSWORD=your_db_password
      - DB_HOST=db
      - DB_PORT=5432
      
    environment:
      POSTGRES_DB: your_db_name
      POSTGRES_USER: your_db_user
      POSTGRES_PASSWORD: your_db_password
      POSTGRES_HOST_AUTH_METHOD: trust
```

### Шаг 4: Сборка контейнеров
```bash
docker-compose build
```

### Шаг 5: Запуск контейнеров
```bash
docker-compose up
```

Приложение будет доступно по адресу http://localhost:8000

```bash
docker-compose down
docker rm -f $(docker ps -a -q)
docker rmi -f $(docker images -q)
docker volume rm $(docker volume ls -q)
```