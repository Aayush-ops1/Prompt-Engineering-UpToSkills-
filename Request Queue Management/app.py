import asyncio
from fastapi import FastAPI, HTTPException

from models import RequestTask
from queue_manager import (
    add_task,
    get_queue_size,
)
from worker import worker

app = FastAPI(
    title="Request Queue Management System"
)


@app.on_event("startup")
async def startup_event():

    # Start multiple workers

    for i in range(3):

        asyncio.create_task(
            worker(i + 1)
        )

    print("Workers Started")


@app.get("/")
async def home():

    return {
        "message":
        "Request Queue Manager Running"
    }


@app.post("/submit")
async def submit_task(task: RequestTask):

    try:

        await add_task(task)

        return {
            "status": "queued",
            "task_id": task.task_id,
            "priority": task.priority
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.get("/queue-status")
async def queue_status():

    return {
        "queue_size":
        get_queue_size()
    }