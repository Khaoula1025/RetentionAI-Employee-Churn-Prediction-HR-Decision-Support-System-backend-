import pandas as pd 
from fastapi import APIRouter,Request,Depends
from sqlalchemy.orm import Session
from app.schemas.prediction import predictionRequest
from app.db.session import get_db
from app.services.llm_service import predict_probability
predictionRouter=APIRouter()

@predictionRouter.post('/predict')
def  make_prediction(predict:predictionRequest,db : Session = Depends(get_db)):
    result = predict_probability(predict.model_dump())
    return {'churn_probability':result[1]}