from fastapi import FastAPI,APIRouter
from app.db.session import Base,engine
from app.api.v1.endpoints.auth import authRouter 

app=FastAPI(
    description="Retention Ai "
)
Base.metadata.create_all(bind=engine)

app.include_router(authRouter)
