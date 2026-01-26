from sqlmodel import SQLModel, Field

class TaskBase(SQLModel):
    title: str
    description: str | None = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int

class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)