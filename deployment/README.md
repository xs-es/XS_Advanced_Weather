# Deployment Guide for Advanced Weather Application

## Docker Deployment

1. Build the Docker image:
    ```bash
    docker build -t weather-app .
    ```

2. Run the container:
    ```bash
    docker run -p 5000:5000 -p 8080:8080 weather-app
    ```

## Docker Compose

To run the entire stack, including the database:

```bash
docker-compose up
```

## Kubernetes Deployment

Ensure that your cluster is running.
Apply the deployment file:
```bash
kubectl apply -f weather_app_deployment.yaml
```