"""Project resource routes."""
from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..services import project_service

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("", response_model=list[schemas.ProjectResponse], status_code=status.HTTP_200_OK)
def list_projects(
    status_filter: schemas.project_status | None = Query(default=None, alias="status"),
    db: Session = Depends(get_db),
) -> list[schemas.ProjectResponse]:
    return project_service.list_projects(db=db, status_filter=status_filter)


@router.get("/{project_id}", response_model=schemas.ProjectResponse, status_code=status.HTTP_200_OK)
def get_project(project_id: int, db: Session = Depends(get_db)) -> schemas.ProjectResponse:
    return project_service.get_project(db=db, project_id=project_id)


@router.post("", response_model=schemas.ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project_in: schemas.ProjectCreate,
    db: Session = Depends(get_db),
) -> schemas.ProjectResponse:
    return project_service.create_project(db=db, project_in=project_in)


@router.put("/{project_id}", response_model=schemas.ProjectResponse, status_code=status.HTTP_200_OK)
def update_project(
    project_id: int,
    project_in: schemas.ProjectUpdate,
    db: Session = Depends(get_db),
) -> schemas.ProjectResponse:
    return project_service.update_project(db=db, project_id=project_id, project_in=project_in)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)) -> Response:
    project_service.delete_project(db=db, project_id=project_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT) 