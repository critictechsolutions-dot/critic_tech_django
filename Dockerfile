# Use official Python image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends

# Copy requirements to container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy Django project files into container
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Set environment variables (optional, for best practice)
ENV PYTHONUNBUFFERED=1

# Expose the port you plan to use (default 8000 for Gunicorn)
EXPOSE 8000

# Start Gunicorn server for Django
CMD ["gunicorn", "critic_tech_django.wsgi:application", "--bind", "0.0.0.0:8000"]
