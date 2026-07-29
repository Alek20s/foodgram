# Foodgram --- Grocery Assistant

## Description

Foodgram is a recipe-sharing platform where users can publish recipes,
add them to favorites, subscribe to other authors, and download shopping
lists.

## Technology Stack

-   Python 3.11
-   Django 5.1
-   Django REST Framework
-   PostgreSQL
-   Docker
-   Nginx
-   GitHub Actions

## Running the Project

### Requirements

-   Docker
-   Docker Compose

### Local Setup

Clone the repository:

``` bash
git clone https://github.com/Alek20s/foodgram.git
cd foodgram
```

Create an `.env` file in the `infra/` directory based on `.env.example`:

``` bash
cp infra/.env.example infra/.env
```

Edit the `.env` file with your own values.

Start the containers from the `infra/` directory:

``` bash
cd infra
docker-compose up -d
```

Apply database migrations:

``` bash
docker-compose exec backend python manage.py migrate
```

Load the ingredients database:

``` bash
docker-compose exec backend python manage.py load_ingredients
```

Create a superuser:

``` bash
docker-compose exec backend python manage.py createsuperuser
```

Collect static files:

``` bash
docker-compose exec backend python manage.py collectstatic --no-input
```

## Service Access

-   Frontend: http://localhost/
-   API documentation: http://localhost/api/docs/
-   Admin panel: http://localhost/admin/

## Deployment

The project is automatically deployed to the server via GitHub Actions
whenever changes are pushed to the `main` branch.

### GitHub Secrets

Configure the following repository secrets:

  Secret            Description
  ----------------- ------------------------------------
  DOCKER_USERNAME   Docker Hub username
  DOCKER_PASSWORD   Docker Hub password
  HOST              Server IP address
  USER              Server username
  SSH_KEY           Private SSH key
  TELEGRAM_TO       Telegram chat ID for notifications
  TELEGRAM_TOKEN    Telegram bot token

### Server `.env` File

Create `~/foodgram/.env` with the following variables:

``` env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-server-ip localhost 127.0.0.1

POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=your-password
DB_HOST=db
DB_PORT=5432

DOCKER_USERNAME=your-dockerhub-username
```

## Demo

Project URL: http://158.160.201.93/

### Admin Credentials

-   **Email:** aleksksn@yahoo.co.uk
-   **Password:** Foodgram2026

## Author

**Alexei Kosyhin**
