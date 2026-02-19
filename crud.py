from sqlalchemy.orm import Session
import models
import schemas

def create_task(db:Session, task:schemas.TaskCreate):
    db_task = models.Task(
        title = task.title,
        description = task.description
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# ✅ get all tasks
def get_tasks(db: Session):

    return db.query(models.Task).all()


# ✅ get single task
def get_task(db: Session, task_id: int):

    return db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()


def update_tasks(db:Session, task_id:int, task:schemas.TaskCreate):
    db_task = get_task(db, task_id)
    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    return db_task

def delete_task(db: Session, task_id: int):

    db_task = get_task(db, task_id)

    db.delete(db_task)

    db.commit()


def mark_complete(db: Session, task_id: int):

    db_task = get_tasks(db, task_id)

    db_task.completed = True

    db.commit()

    return db_task
