# tests/test_model.py
import pytest
import joblib
from types import SimpleNamespace

from app.services.llm_service import predict_probability

# Load the model saved with joblib
model = joblib.load("ml.models.probModel.pkl")

def test_model_loaded():
    # Check that model object exists and has expected attributes
    assert model is not None
    assert hasattr(model, "predict")
    assert hasattr(model, "predict_proba")
    assert hasattr(model, "feature_names_in_")  # scikit-learn >=0.24

def test_predict_probability_consistency():
    # Example input data matching model features
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
    
    # Ensure prediction is a valid probability
    assert 0.0 <= prob <= 1.0

    # Optional: check expected range for low-risk input
    assert 0.0 <= prob <= 0.5
