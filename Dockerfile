# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set environment variable to avoid buffering of output (optional, but useful for debugging)
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies inside the container
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Expose port 8000 to make the app accessible on the host machine
EXPOSE 8000

# Command to run the Django application (adjust as needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
