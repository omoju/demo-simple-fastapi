# FastAPI Hello World Demo

A lightweight, high-performance API demonstration showcasing the power and simplicity of FastAPI.

## Features

- Interactive Swagger UI documentation
- Simple "Hello World" endpoint
- Health check endpoint
- Pydantic models for response validation

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Installation

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn
```

## Running the Application

```bash
# Run directly with Python
python main.py

# Alternatively, run with Uvicorn
uvicorn main:app --reload
```

## API Documentation

Once the server is running, you can access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

- `GET /`: Returns "Hello World" message
- `GET /health`: Health check endpoint

## Docker Deployment

```bash
# Build the Docker image
docker build -t fastapi-hello-world .

# Run the container
docker run -p 8000:8000 fastapi-hello-world
```
