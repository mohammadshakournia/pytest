# Task API

A simple REST API for creating and viewing tasks using FastAPI and pytest.

## Features

- Create a task
- Get all tasks
- Get one task by ID
- Validate task titles and priorities
- Test successful and invalid requests

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

On Windows:

```powershell
.venv\Scripts\activate
```

On macOS and Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the API

Start the server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Create a task

```http
POST /tasks
```

Example request body:

```json
{
  "title": "Learn pytest",
  "priority": "high"
}
```

Allowed priorities:

```text
low
medium
high
```

### Get all tasks

```http
GET /tasks
```

### Get one task

```http
GET /tasks/{task_id}
```

Example:

```http
GET /tasks/1
```

## Run Tests

Run all automated tests with:

```bash
pytest -v
```

## Project Files

### `app/main.py`

Contains the main application code. It defines the data models, API endpoints, validation rules, and temporary in-memory storage.

### `app/__init__.py`

Marks the `app` folder as a Python package.

### `tests/test_tasks_api.py`

Contains the automated API tests. These tests check task creation, task retrieval, validation errors, and missing tasks.

### `tests/conftest.py`

Contains shared test setup. It creates the test client and resets the stored tasks before each test.

### `tests/__init__.py`

Marks the `tests` folder as a Python package.

### `requirements.txt`

Contains the Python packages required to run the application and its tests.

### `pytest.ini`

Contains pytest configuration, such as the location and naming format of test files.

### `.gitignore`

Lists files and folders that should not be committed to Git, such as virtual environments and Python cache files.

## Notes

This project stores tasks in memory. All data will be lost when the application stops.

The main purpose of this project is to demonstrate API development and automated testing with pytest.
