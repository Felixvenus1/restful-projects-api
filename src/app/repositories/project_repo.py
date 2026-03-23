"""Project repository data access functions."""
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas


def create_project(db: Session, project_in: schemas.ProjectCreate) -> models.Project:
    project = models.Project(**project_in.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projects(db: Session, status: str | None = None) -> list[models.Project]:
    stmt = select(models.Project)

    if status is not None:
        stmt = stmt.where(models.Project.status == status)

    stmt = stmt.order_by(models.Project.id.asc())
    return list(db.scalars(stmt).all())


def get_project_by_id(db: Session, project_id: int) -> models.Project | None:
    stmt = select(models.Project).where(models.Project.id == project_id)
    return db.scalar(stmt)


def update_project(
    db: Session,
    project: models.Project,
    project_in: schemas.ProjectUpdate,
) -> models.Project:
    update_data = project_in.model_dump(exclude_unset=True)

    for field_name, value in update_data.items():
        setattr(project, field_name, value)

    db.commit()
    db.refresh(project)
    return project


def delete_project(db: Session, project: models.Project) -> None:
    db.delete(project)
    db.commit()