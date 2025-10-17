# Base image
FROM python:3.12-slim

# Workdir
WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y libpq-dev build-essential && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY notebook/requirements.txt /app/requirements.txt

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY notebook /app/notebook/

# Collect static (optional, depends on WhiteNoise/Nginx)
RUN python /app/notebook/manage.py collectstatic --noinput

EXPOSE 8000

WORKDIR /app/notebook

# Gunicorn entrypoint
CMD ["gunicorn", "notebook.wsgi:application", "--bind", "0.0.0.0:8000"]
