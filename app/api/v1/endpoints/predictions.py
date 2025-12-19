import pandas as pd 
from fastapi import APIRouter,Request,Depends
from sqlalchemy.orm import Session
from app.schemas.prediction import predictionRequest
from app.db.session import get_db
from app.services.llm_service import predict_probability
from app.api.deps import get_current_user
from app.models.employe import Employee
from app.models.predictions_history import PredictionHistory
predictionRouter=APIRouter()

@predictionRouter.post('/predict')
def  make_prediction(predict:predictionRequest,db : Session = Depends(get_db),current_user:str=Depends(get_current_user)):
        prediction=predict.model_dump()
        result = predict_probability(prediction)
        probability_value = float(result)
        employee=Employee(**prediction)
        db.add(employee)
        db.flush()
        record_history =PredictionHistory(user_id=current_user.id,employee_id=employee.id,probability=probability_value)
        db.add(record_history)
        db.commit()
        return {'churn_probability':result}
