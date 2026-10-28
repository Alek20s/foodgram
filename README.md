# Foodgram — Recipe Sharing Platform

Foodgram is a web application for sharing recipes. Users can publish recipes, add recipes to their favourites, follow other authors, and generate shopping lists.

This project demonstrates Python web development, REST API implementation, relational database integration, containerisation, and automated deployment. It complements my separate Django testing project, which focuses specifically on automated tests.

## Key Features

- Create and publish recipes.
- Add recipes to favourites.
- Subscribe to other authors.
- Generate shopping lists from selected recipes.
- Access functionality through a REST API.
- Explore endpoints using interactive API documentation.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Programming language |
| Django 5.1 | Web framework |
| Django REST Framework | REST API |
| PostgreSQL | Relational database |
| Docker and Docker Compose | Containerisation |
| Nginx | Web server |
| GitHub Actions | CI/CD |
| API documentation | Available at `/api/docs/` |

## Relevance to Software Test Analyst Roles

Foodgram provides a practical web application and REST API suitable for understanding and validating end-to-end application behaviour.

Relevant QA areas include:

- **REST API testing:** request data, response codes, and error handling.
- **Data validation:** checking recipe data and application rules.
- **Database testing:** persistence and relationships between users, recipes, favourites, and subscriptions.
- **Authentication and permissions:** access to protected actions and user-specific data.
- **Integration and deployment:** running Docker containers and using a GitHub Actions workflow.
- **API exploration:** inspecting endpoints and request formats through interactive documentation.

These are potential testing areas, not claims that the project includes a separate automated API test suite, Selenium tests, or Postman collections.

## Project Setup

### Requirements

- Docker
- Docker Compose

### Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Alek20s/foodgram.git
   cd foodgram
   ```

2. Create the environment file:

   ```bash
   cp infra/.env.example infra/.env
   ```

3. Edit `infra/.env` and provide your configuration values.

4. Start the services:

   ```bash
   cd infra
   docker-compose up -d
   ```

5. Apply database migrations:

   ```bash
   docker-compose exec backend python manage.py migrate
   ```

6. Load the ingredients data:

   ```bash
   docker-compose exec backend python manage.py load_ingredients
   ```

7. Create an administrator account if required:

   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

8. Collect static files:

   ```bash
   docker-compose exec backend python manage.py collectstatic --no-input
   ```

## Local Service URLs

| Service | URL |
|---|---|
| Application | [http://localhost/](http://localhost/) |
| API documentation | [http://localhost/api/docs/](http://localhost/api/docs/) |
| Django admin | [http://localhost/admin/](http://localhost/admin/) |

## Deployment

The project is configured to deploy to a server through GitHub Actions when changes are pushed to the `main` branch.

Depending on the workflow, configure the required GitHub repository secrets, such as:

| Secret | Purpose |
|---|---|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub password or access token |
| `HOST` | Deployment server address |
| `USER` | SSH username |
| `SSH_KEY` | SSH private key |
| `TELEGRAM_TO` | Notification destination |
| `TELEGRAM_TOKEN` | Telegram bot token |

The server environment file should contain deployment-specific settings, including `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and database credentials. Never commit passwords, tokens, or private keys to the repository.

## Demo

[Open the deployed application](http://158.160.201.93/)

## Related Project

See my Django Automated Testing project for examples of pytest, Django test-client checks, route and permission testing, and regression testing.

## Author

Alexei Kosyhin