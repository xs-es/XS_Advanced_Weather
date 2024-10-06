# Dockerfile

# Use Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose ports for Flask API and UI
EXPOSE 5000 8080

# Environment variables for config
ENV DEBUG=True
ENV SECRET_KEY=supersecretkey

# Command to run the application
CMD ["python", "main.py"]
