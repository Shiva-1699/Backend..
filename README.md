# Django Multilingual FAQ System with WYSIWYG Editor

This project implements a multilingual FAQ system using Django. The system includes support for a WYSIWYG (What You See Is What You Get) editor, REST APIs, caching with Redis, and Google Translate integration. The application is containerized using Docker.

## Features

- **Multilingual Support**: Translates FAQs into multiple languages using Google Translate API.
- **WYSIWYG Editor**: A user-friendly editor to create and manage FAQ content.
- **REST APIs**: Endpoints for CRUD operations on FAQs.
- **Caching**: Redis caching for performance optimization.
- **Dockerized**: The project is containerized with Docker for easy deployment.

## Requirements

- Docker
- Docker Compose

## Setup Instructions

Follow the steps below to set up the project:

### 1. Clone the repository

```bash
git clone <repository_url>
cd <project_folder>
2. Build the Docker image
Build the Docker image using the following command:

bash
Copy
Edit
docker-compose build
3. Run the Docker containers
Start the project by running the following command:

bash
Copy
Edit
docker-compose up
This will start the Django application and other services (e.g., Redis) defined in the docker-compose.yml file.

4. Access the Application
Once the containers are up and running, you can access the application at http://localhost:8000.

Environment Variables
Ensure you have the following environment variables set in your .env file:

DJANGO_SECRET_KEY: A secret key for Django.
DATABASE_URL: URL for your database connection.
REDIS_URL: URL for your Redis instance.
GOOGLE_TRANSLATE_API_KEY: API key for Google Translate integration.
API Endpoints
List FAQs
GET /api/faqs/
Create FAQ
POST /api/faqs/
Retrieve FAQ
GET /api/faqs/{id}/
Update FAQ
PUT /api/faqs/{id}/
Delete FAQ
DELETE /api/faqs/{id}/
Testing
Run unit tests with the following command:

bash
Copy
Edit
docker-compose run web pytest
Deployment
To deploy this application to a production environment, follow these steps:

Build the Docker image: docker-compose build
Push the image to a Docker registry (e.g., Docker Hub or AWS ECR).
Deploy the image to your preferred cloud provider (e.g., AWS, Azure).
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Create a new pull request.
