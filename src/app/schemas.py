from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

project_status = Literal["planned", "pending", "complete"]

class ProjectBase(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=120,
        description="Project name.",
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Project details.",
    )
    status: project_status = Field(
        default="planned",
        description="Lifecycle status.",
    )


#class ProjectCreate(ProjectBase):
    


class ProjectUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=120,
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
    )
    status: project_status | None = Field(
        default=None,
        description="status update.",
    )


class ProjectResponse(ProjectBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    updated_at: datetime