from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Project API",
    version="0.1.0",
    description="RESTful CRUD API for project records.",
    lifespan=lifespan,
)


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}