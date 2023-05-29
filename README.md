# Django Weather App

This Django application provides real-time temperature information for a given city or defaults to New York if no city is specified. The temperature data is retrieved from Google as the primary source of information.

## Usage

To access the temperature information, make a GET request to the `/weather/<city_name>` endpoint. Include the desired city name as a parameter to retrieve the temperature for that city. If no city parameter is provided, the application will return the temperature for New York.

The temperature data is cached in Redis for a duration of 1 minute. Subsequent requests for the same city within this timeframe will retrieve the temperature from the cache, reducing the reliance on external API calls.

## Dependencies

- Python 3.10
- Django 4.2.1: The web framework used to develop this application.
- Redis 4.5.5: Used as a caching mechanism for storing temperature data.
- Google Search: The primary source of temperature information.

## Installation

To install and run this Django Weather App locally using Docker containers, follow these steps:

1. Clone the repository from GitHub.
2. Install Docker and Docker Compose on your machine.
3. Create an `.env` file in the root directory and configure the necessary environment variables. Here's an example of the `.env` file contents:


```plaintext
SECRET_KEY=SomeSecretString
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
REDIS_HOST='redis'
REDIS_PORT=6379
CITY='New York'
```

4. Build and run the Docker containers using Docker Compose.

```bash
$ git clone <repository_url>
$ cd <repository_directory>
$ # Configure environment variables in .env file
$ docker-compose up --build
```

Ensure that you have adjust the environment variables in the `.env` file accordingly.

## Docker Compose Configuration
The `docker-compose.yml` file defines two services: web and redis.

## Service: web
- Container Name: `app`
- Build: Builds the Docker image using the Dockerfile located in `./app_django`.
- Command: Runs the Django development server (`python manage.py runserver 0.0.0.0:8000`).
- Volumes: Mounts the local `./app_django/` directory to the `/app/` directory inside the container.
- Ports: Forwards the container's port `8000` to the host's port `4000`.
- Environment File: Loads the environment variables from `./.env`.

## Service: redis
- Container Name: `redis`
- Image: Uses the official Redis Docker image.
- Ports: Forwards the container's port `6379` to the host's port `6379`.
- Contributions
- Contributions to this project are welcome! If you have any suggestions, bug fixes, or additional features to propose, feel free to open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License.