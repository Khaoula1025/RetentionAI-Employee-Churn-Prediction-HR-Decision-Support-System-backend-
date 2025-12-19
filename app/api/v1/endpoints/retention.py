from fastapi import APIRouter , Depends
from app.schemas.prediction import predictionRequest
from sqlalchemy.orm import Session 
from app.db.session import get_db
from app.services.llm_service import predict_probability
from app.services.retention_service import gemini_analyse
retentionRouter=APIRouter()

@retentionRouter.post('/retention')
def retention_maker(predict:predictionRequest,db : Session = Depends(get_db)):
    predictionData=predict.model_dump()
    probability=predict_probability(predictionData)
    retention=gemini_analyse(probability,predictionData)

    return retention

