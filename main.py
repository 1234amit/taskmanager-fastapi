from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Task Manager API")

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#create task
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):

    return crud.create_task(db, task)

#get all task
@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db:Session = Depends(get_db)):
    return crud.get_tasks(db)


#get task by id
# Get Single Task

@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):

    return crud.get_task(db, task_id)


# Update Task

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):

    return crud.update_tasks(db, task_id, task)


# Delete Task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    crud.delete_task(db, task_id)

    return {"message": "Task deleted"}


# Mark Complete

@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int, db: Session = Depends(get_db)):

    return crud.mark_complete(db, task_id)


