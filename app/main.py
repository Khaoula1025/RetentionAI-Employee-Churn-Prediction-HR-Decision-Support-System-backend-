from fastapi import FastAPI,APIRouter
from app.db.session import Base,engine
from app.api.v1.endpoints.auth import authRouter 
from app.api.v1.endpoints.predictions import predictionRouter 
from app.api.v1.endpoints.retention import retentionRouter  

app=FastAPI(
    description="Retention Ai "
)
Base.metadata.create_all(bind=engine)

app.include_router(authRouter)
app.include_router(predictionRouter)
app.include_router(retentionRouter)
