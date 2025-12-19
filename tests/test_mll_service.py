from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app
from types import SimpleNamespace
from app.api.deps import get_current_user

def override_get_current_user():
    return SimpleNamespace(id=1, email="test@test.com")

app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

test_data_high_risk = {
    "Age": 32,
    "BusinessTravel": "Travel_Rarely",
    "DailyRate": 1100,
    "Department": "Research & Development",
    "DistanceFromHome": 18,
    "Education": 3,
    "EducationField": "Life Sciences",
    "EnvironmentSatisfaction": 2,
    "Gender": "Female",
    "JobInvolvement": 2,
    "JobLevel": 2,
    "JobRole": "Research Scientist",
    "JobSatisfaction": 2,
    "MaritalStatus": "Single",
    "MonthlyIncome": 4200,
    "MonthlyRate": 14500,
    "NumCompaniesWorked": 3,
    "OverTime": "Yes",
    "PercentSalaryHike": 11,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 2,
    "StockOptionLevel": 0,
    "TotalWorkingYears": 8,
    "WorkLifeBalance": 2,
    "YearsAtCompany": 4,
    "YearsInCurrentRole": 3,
    "YearsSinceLastPromotion": 3,
    "YearsWithCurrManager": 2
}


@patch("app.api.v1.endpoints.retention.gemini_analyse")
@patch("app.api.v1.endpoints.retention.predict_probability")
def test_retention_high_risk(mock_predict_probability, mock_gemini_analyse):
   
    mock_predict_probability.return_value = 0.75
    mock_gemini_analyse.return_value = {
        "churn_probability": 0.75,
        "retention_actions": (
            "Action 1 : Ajuster la charge de travail.\n"
            "Action 2 : Revoir le package de rémunération.\n"
            "Action 3 : Mettre en place un plan de carrière."
        )
    }
    response = client.post("/retention", json=test_data_high_risk)
    assert response.status_code == 200
    data = response.json()
    assert data["churn_probability"] == 0.75
    assert "retention_actions" in data
    mock_predict_probability.assert_called_once()
    mock_gemini_analyse.assert_called_once()
