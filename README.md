# AR2EN Docker

A containerized Arabic to English translation service built with Flask and Hugging Face Transformers.

## Overview

This project provides a REST API for translating Arabic text to English using the Helsinki-NLP/opus-mt-ar-en translation model from Hugging Face. The service is containerized using Docker for easy deployment and scaling.

## Features

- RESTful API for Arabic to English translation
- Asynchronous processing with task ID tracking
- Dockerized application for easy deployment
- Based on the Helsinki-NLP/opus-mt-ar-en machine translation model

## Requirements

- Docker
- Python 3.10 (if running locally)
- Dependencies listed in requirements.txt

## Installation

### Using Docker (Recommended)

1. Clone this repository:
   ```
   git clone https://github.com/Begolosamazaref/AR2EN-Docker.git
   cd AR2EN_Docker
   ```

2. Build the Docker image:
   ```
   docker build -t ar2en-translator .
   ```

3. Run the container:
   ```
   docker run -p 5000:5000 ar2en-translator
   ```

The API will be available at http://localhost:5000

### Local Installation

1. Clone the repository and navigate to the project folder
2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python AR2EN_FlaskApi.py
   ```

## API Usage

### Translate Text

**Endpoint:** `POST /translate/ar2en`

**Request Body:**
```json
{
    "text": "مرحبا بالعالم"
}
```

**Response:**
```json
{
    "task_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

### Check Translation Status

**Endpoint:** `GET /translate/ar2en/status/<task_id>`

**Response (Processing):**
```json
{
    "status": "processing",
    "result": null
}
```

**Response (Completed):**
```json
{
    "status": "completed",
    "result": "Hello world"
}
```

## How it Works

1. The application loads the MarianMT translation model during startup
2. When a translation request is received, a unique task ID is generated
3. The translation process runs asynchronously in a separate thread
4. Clients can check the status of their translation using the task ID
5. Once complete, the translation result can be retrieved

## License

MIT License

## Contact

Begolosamazaref on GitHub
