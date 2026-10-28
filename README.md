Foodgram — Recipe Sharing Platform
Foodgram is a web application for sharing recipes. Users can publish recipes, add recipes to their favourites, follow other authors, and generate shopping lists.

This project demonstrates Python web development, REST API implementation, relational database integration, containerisation, and automated deployment. It complements my separate Django testing project, which focuses specifically on automated tests.
Key Features
- Create and publish recipes.
- Add recipes to favourites.
- Subscribe to other authors.
- Generate a shopping list from selected recipes.
- Access the application through a REST API.
- Explore API endpoints using the interactive API documentation.
Technology Stack
- Language: Python 3.11
- Web framework: Django 5.1
- API: Django REST Framework
- Database: PostgreSQL
- Containers: Docker and Docker Compose
- Web server: Nginx
- CI/CD: GitHub Actions
- API documentation: Available at /api/docs/
Relevance to Software Test Analyst Roles
Foodgram provides a practical web application and REST API that can be used to understand and validate end-to-end application behaviour.

Relevant areas for quality assurance include:
- REST API behaviour: checking endpoint responses, request data, status codes, and error handling.
- Data validation: checking that recipes and related data follow application rules.
- Database-backed functionality: verifying persistence and relationships between users, recipes, favourites, and subscriptions.
- Authentication and permissions: checking access to protected actions and user-specific data.
- Integration and deployment: running the application in Docker containers and deploying changes through a GitHub Actions workflow.
- API exploration: using the interactive API documentation to inspect available endpoints and expected request formats.
The repository's documented technology stack demonstrates API and database development. These points describe areas suitable for testing; they should not be interpreted as claims that a separate automated API test suite, Selenium tests, or Postman collections are included.
Project Setup
Requirements
- Docker
- Docker Compose
Run Locally
1. Clone the repository:
   git clone https://github.com/Alek20s/foodgram.git
   cd foodgram
2. Create an environment file from the example:
   cp infra/.env.example infra/.env
3. Edit infra/.env and provide your own configuration values.
4. Start the services:
   cd infra
   docker-compose up -d
5. Apply database migrations:
   docker-compose exec backend python manage.py migrate
6. Load the ingredients data:
   docker-compose exec backend python manage.py load_ingredients
7. Create an administrator account when required:
   docker-compose exec backend python manage.py createsuperuser
8. Collect static files:
   docker-compose exec backend python manage.py collectstatic --no-input
Local Service URLs
- Application: http://localhost/
- Interactive API documentation: http://localhost/api/docs/
- Django admin: http://localhost/admin/
Deployment
The project is configured to deploy to a server through GitHub Actions when changes are pushed to the main branch.

Configure deployment credentials as GitHub repository secrets rather than storing them in source code. Depending on the workflow configuration, these may include:
Secret	Purpose
DOCKER_USERNAME	Docker Hub username
DOCKER_PASSWORD	Docker Hub password or access token
HOST	Deployment server address
USER	SSH username for the server
SSH_KEY	SSH private key used by the deployment workflow
TELEGRAM_TO	Destination for deployment notifications
TELEGRAM_TOKEN	Telegram bot token for notifications


The server environment file should contain deployment-specific values such as SECRET_KEY, DEBUG, ALLOWED_HOSTS, and database credentials. Use your own values and never commit secrets to the repository.
Demo
Project: http://158.160.201.93/
Related Project
See my Django Automated Testing project for examples focused on pytest, Django test-client checks, route and permission testing, and regression testing.
Author
Alexei Kosyhin