from pydantic import BaseModel

class RequestTask(BaseModel):
    task_id: str
    priority: int
    data: str