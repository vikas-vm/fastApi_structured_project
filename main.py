from fastapi import FastAPI, Request, Response
from app.api import api_router
from app.conf import settings
from app.conf.database import SessionLocal, Base, engine

app = FastAPI(
    title=settings.PROJECT_NAME, debug=settings.DEBUG
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

Base.metadata.create_all(bind=engine)
