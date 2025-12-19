import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.prediction import predictionRequest
from app.db.session import get_db
from app.services.llm_service import predict_probability
from app.api.deps import get_current_user
from app.models.employe import Employee
from app.models.predictions_history import PredictionHistory

predictionRouter = APIRouter()

@predictionRouter.post("/predict")
def make_prediction(
    predict: predictionRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        # Convert Pydantic model to dict
        prediction_data = predict.model_dump()

        # ML / LLM prediction
        try:
            result = predict_probability(prediction_data)
            probability_value = float(result)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Prediction service failed: {str(e)}"
            )

        # Save employee data
        employee = Employee(**prediction_data)
        db.add(employee)
        db.flush()  # get employee.id

        # Save prediction history
        history = PredictionHistory(
            user_id=current_user.id,
            employee_id=employee.id,
            probability=probability_value
        )
        db.add(history)

        db.commit()

        return {
            "churn_probability": probability_value
        }

    except HTTPException:
        db.rollback()
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected server error: {str(e)}"
        )
