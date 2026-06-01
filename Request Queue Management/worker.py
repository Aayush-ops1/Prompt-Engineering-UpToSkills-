import asyncio
import logging

from queue_manager import get_task

logging.basicConfig(level=logging.INFO)


async def worker(worker_id):

    while True:

        priority, task = await get_task()

        logging.info(
            f"[Worker-{worker_id}] Processing Task "
            f"{task.task_id}"
        )

        # Simulate processing
        await asyncio.sleep(5)

        logging.info(
            f"[Worker-{worker_id}] Completed Task "
            f"{task.task_id}"
        )