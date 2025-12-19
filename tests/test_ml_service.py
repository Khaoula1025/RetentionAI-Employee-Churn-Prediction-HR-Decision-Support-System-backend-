import pytest
import joblib
from types import SimpleNamespace

from app.services.llm_service import predict_probability

model=joblib.load('ml/models/probModel.pkl')

def test_model_loaded():
    assert model is not None
    assert hasattr(model, "predict")
    assert hasattr(model, "predict_proba")
    assert hasattr(model, "feature_names_in_") 

def test_predict_probability_consistency():
    test_input = {
        "Age": 30,
        "BusinessTravel": "Travel_Rarely",
        "DailyRate": 1000,
        "Department": "Research & Development",
        "DistanceFromHome": 10,
        "Education": 3,
        "EducationField": "Life Sciences",
        "EnvironmentSatisfaction": 3,
        "Gender": "Female",
        "JobInvolvement": 3,
        "JobLevel": 2,
        "JobRole": "Research Scientist",
        "JobSatisfaction": 3,
        "MaritalStatus": "Married",
        "MonthlyIncome": 5000,
        "MonthlyRate": 15000,
        "NumCompaniesWorked": 2,
        "OverTime": "No",
        "PercentSalaryHike": 12,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": 3,
        "StockOptionLevel": 1,
        "TotalWorkingYears": 8,
        "WorkLifeBalance": 3,
        "YearsAtCompany": 5,
        "YearsInCurrentRole": 3,
        "YearsSinceLastPromotion": 2,
        "YearsWithCurrManager": 3
    }

    prob = predict_probability(test_input)
    
    assert 0.0 <= prob <= 1.0


