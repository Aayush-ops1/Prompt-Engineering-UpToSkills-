import asyncio
import logging

logging.basicConfig(level=logging.INFO)

MAX_QUEUE_SIZE = 100

queue = asyncio.PriorityQueue(maxsize=MAX_QUEUE_SIZE)


async def add_task(task):
    """
    Add task to queue
    """

    if queue.full():
        raise Exception("Queue Overflow")

    await queue.put((task.priority, task))

    logging.info(
        f"Task Added -> ID={task.task_id}, Priority={task.priority}"
    )


async def get_task():
    """
    Get next task
    """

    return await queue.get()


def get_queue_size():
    return queue.qsize()