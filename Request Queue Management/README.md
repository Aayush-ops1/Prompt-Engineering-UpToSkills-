# Request Queue Management System

## Overview

This project implements a backend queue management system using FastAPI and Python asyncio.

Features:

- Asynchronous Request Queue
- Priority Based Scheduling
- Concurrent Workers
- Queue Overflow Protection
- Logging
- REST APIs

## APIs

### GET /

Returns system status.

### POST /submit

Submit a task.

Example:

```json
{
  "task_id": "101",
  "priority": 1,
  "data": "Generate Report"
}
```

### GET /queue-status

Returns current queue size.

## Installation

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app:app --reload
```

Open:

http://127.0.0.1:8000/docs