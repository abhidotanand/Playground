from app.db import config
from app.tasks.models import Task, TaskOut, TaskUpdate
from sqlmodel import Session, select
from fastapi import HTTPException, status

def create_task(task: Task, session: Session) -> TaskOut:
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_task(task_id: int, session: Session) -> TaskOut:
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found.")
    return task

def get_tasks(session: Session) -> list[TaskOut]:
    tasks = session.exec(select(Task)).all()
    return tasks
    
def update_task(task_id: int, updated_task: TaskUpdate, session: Session) -> TaskOut:
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    # task.title = updated_task.title
    # task.description = updated_task.description
    # task.completed = updated_task.completed

    new_task = updated_task.model_dump()
    task.sqlmodel_update(new_task)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def delete_task(task_id: int, session: Session):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    session.delete(task)
    session.commit()
    return task