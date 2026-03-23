"""Project business logic."""
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..repositories import project_repo


def create_project(db: Session, project_in: schemas.ProjectCreate) -> models.Project:
    return project_repo.create_project(db=db, project_in=project_in)


def list_projects(db: Session, status_filter: str | None = None) -> list[models.Project]:
    return project_repo.get_projects(db=db, status=status_filter)


def get_project(db: Session, project_id: int) -> models.Project:
    project = project_repo.get_project_by_id(db=db, project_id=project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found",
        )
    return project


def update_project(
    db: Session,
    project_id: int,
    project_in: schemas.ProjectUpdate,
) -> models.Project:
    project = project_repo.get_project_by_id(db=db, project_id=project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found",
        )

    return project_repo.update_project(db=db, project=project, project_in=project_in)


def delete_project(db: Session, project_id: int) -> None:
    project = project_repo.get_project_by_id(db=db, project_id=project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {project_id} not found",
        )

    project_repo.delete_project(db=db, project=project)