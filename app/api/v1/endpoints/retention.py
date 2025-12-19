from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.prediction import predictionRequest
from app.db.session import get_db
from app.services.llm_service import predict_probability
from app.services.retention_service import gemini_analyse

retentionRouter = APIRouter()

@retentionRouter.post("/retention")
def retention_maker(
    predict: predictionRequest,
    db: Session = Depends(get_db)
):
    try:
        # Convert request data
        prediction_data = predict.model_dump()

        # Get churn probability
        try:
            probability = predict_probability(prediction_data)
            probability_value = float(probability)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Prediction service failed: {str(e)}"
            )

        # Generate retention analysis (Gemini / LLM)
        try:
            retention = gemini_analyse(probability_value, prediction_data)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Retention analysis failed: {str(e)}"
            )

        return retention

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected server error: {str(e)}"
        )
