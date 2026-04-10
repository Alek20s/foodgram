Foodgram — Продуктовый помощник
Описание
Foodgram — сервис для публикации рецептов. Пользователи могут создавать рецепты, добавлять их в избранное, подписываться на других авторов и скачивать список покупок.
Технологии

Python 3.11
Django 5.1
Django REST Framework
PostgreSQL
Docker
Nginx
GitHub Actions

Запуск проекта
Требования

Docker
Docker Compose

Локальный запуск

Клонировать репозиторий:

bashgit clone https://github.com/Alek20s/foodgram.git
cd foodgram

Создать файл .env в папке infra/ на основе .env.example:

bashcp infra/.env.example infra/.env

Заполнить .env своими значениями.
Из папки infra/ запустить контейнеры:

bashcd infra
docker-compose up -d

Выполнить миграции:

bashdocker-compose exec backend python manage.py migrate

Загрузить ингредиенты:

bashdocker-compose exec backend python manage.py load_ingredients

Создать суперпользователя:

bashdocker-compose exec backend python manage.py createsuperuser

Собрать статику:

bashdocker-compose exec backend python manage.py collectstatic --no-input
Доступ к сервису

Фронтенд: http://localhost/
API документация: http://localhost/api/docs/
Админ панель: http://localhost/admin/

Развёртывание на сервере
Проект автоматически разворачивается на сервере через GitHub Actions при пуше в ветку main.
GitHub Secrets
Необходимо добавить следующие секреты в настройках репозитория:
СекретОписаниеDOCKER_USERNAMEИмя пользователя Docker HubDOCKER_PASSWORDПароль Docker HubHOSTIP адрес сервераUSERИмя пользователя сервераSSH_KEYПриватный SSH ключTELEGRAM_TOID Telegram чата для уведомленийTELEGRAM_TOKENТокен Telegram бота
Файл .env на сервере
Создать файл ~/foodgram/.env со следующими переменными:
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-server-ip localhost 127.0.0.1

POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=your-password
DB_HOST=db
DB_PORT=5432

DOCKER_USERNAME=your-dockerhub-username
Демо
Проект доступен по адресу: http://158.160.201.93/
Данные для входа в админку:

Email: aleksksn@yahoo.co.uk
Пароль: Foodgram2026

Автор
Алексей Косыхин