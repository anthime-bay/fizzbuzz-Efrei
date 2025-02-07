# Use official Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt pytest

# Ensure Python can find the modules in /app
ENV PYTHONPATH=/app

# Run tests
CMD ["pytest", "fizzbuzz.py"]