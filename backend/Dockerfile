# Use the official Python 3.10 image as the base image
FROM python:3.10-slim-buster

# Install the specific version of Poetry (1.8.3)
RUN pip install poetry==1.8.3

# Set the working directory inside the container to /backend
WORKDIR /backend

# Copy the Poetry configuration files into the container
COPY pyproject.toml poetry.lock ./

# Copy the source code into the container
COPY src ./src

# Create an empty README.md file in the container
RUN touch README.md

# Install the project dependencies, excluding the development dependencies
RUN poetry install --without dev

# Set the working directory to /src
WORKDIR /backend/src

# Set the entrypoint command to run the application using Poetry and Gunicorn
CMD ["sh", "-c", "poetry run python wsgi.py create_db;poetry run gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app"]