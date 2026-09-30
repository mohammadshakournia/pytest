from typing import Literal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


Priority = Literal["low", "medium", "high"]


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    priority: Priority = "medium"


class Task(TaskCreate):
    id: int
    completed: bool = False


app = FastAPI(title="Task API", version="1.0.0")

tasks: dict[int, Task] = {}
next_task_id = 1


@app.post(
    "/tasks",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
)
def create_task(payload: TaskCreate) -> Task:
    global next_task_id

    task = Task(
        id=next_task_id,
        title=payload.title,
        priority=payload.priority,
    )

    tasks[task.id] = task
    next_task_id += 1

    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task