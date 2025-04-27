# Celery Tutorial

A simple project demonstrating Celery with Redis as a broker for task processing.

## Project Overview

This project demonstrates how to use Celery for distributed task processing with Redis as the message broker. It includes examples of:

- Basic arithmetic tasks
- Simulated slow operations
- Task routing with different queues

## Requirements

- Python 3.12+
- Redis server running on localhost:6379
- uv (Python package manager and virtual environment tool)

## Setup

1. Clone this repository
2. Create and activate a virtual environment using uv:

```bash
uv venv
source .venv/bin/activate  # On Linux/MacOS
```

3. Install dependencies:

```bash
uv pip install .
```

## Running the Application

### Start Redis

Make sure Redis is running on localhost:6379.

### Start the Celery Worker

To start the Celery worker:

```bash
uv run celery -A worker worker
```

For additional worker options (like specifying queues, concurrency):

```bash
uv run celery -A worker worker -Q default,fast_queue,slow_queue -c 4
```

### Run the Main Application

To run the main application that sends tasks to the workers:

```bash
uv run python main.py
```

## Project Structure

- `main.py` - Main application that calls Celery tasks
- `worker/` - Celery app and task definitions
  - `celery.py` - Celery configuration
  - `tasks/` - Task definitions
    - `math_tasks.py` - Simple arithmetic tasks
    - `processing_tasks.py` - Simulated processing tasks

## Using uv

This project uses [uv](https://github.com/astral-sh/uv) for package management and virtual environments. uv is a faster alternative to pip and virtualenv.

Key uv commands:
```bash
# Install packages
uv pip install <package>

# Run Python commands
uv run python <script.py>

# Run any installed command
uv run <command>
```
