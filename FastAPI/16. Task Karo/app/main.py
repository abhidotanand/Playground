from fastapi import FastAPI, status
from app.db.config import create_db_and_tables
from contextlib import asynccontextmanager
from app.tasks.services import *
from app.tasks.models import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    create_db_and_tables()
    yield
    print("Application shutdown")

app = FastAPI(lifespan=lifespan)

@app.post("/task", status_code=status.HTTP_201_CREATED, response_model=TaskOut)
def new_task(new_task: TaskCreate):
    task = Task(title=new_task.title, description=new_task.description, completed=new_task.completed)
    created_task = create_task(task)
    return created_task

@app.get("/tasks", status_code=status.HTTP_200_OK, response_model=list[TaskOut])
def get_all_tasks():
    tasks = get_tasks()
    return tasks

@app.get("/task/{task_id}", status_code=status.HTTP_200_OK)
def get_single_task(task_id: int):
    task = get_task(task_id)
    return task

@app.put("/task/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskOut)
def update_existing_task(task_id: int, updated_task: TaskUpdate):
    task_data = Task(title=updated_task.title, description=updated_task.description, completed=updated_task.completed)
    updated = update_task(task_id, task_data)
    return updated

@app.delete("/task/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_task(task_id: int):
    deleted_task = delete_task(task_id)
    return deleted_task