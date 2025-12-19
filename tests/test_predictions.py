from types import SimpleNamespace
from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app
from app.api.deps import get_current_user

client = TestClient(app)

# ---- Mock authenticated user ----
def override_get_current_user():
    return SimpleNamespace(id=1, email="test@test.com")

app.dependency_overrides[get_current_user] = override_get_current_user


def test_prediction_with_mocked_llm():
    test_input = {
        "Age": 45,
        "BusinessTravel": "Travel_Frequently",
        "DailyRate": 800,
        "Department": "Sales",
        "DistanceFromHome": 25,
        "Education": 2,
        "EducationField": "Marketing",
        "EnvironmentSatisfaction": 1,
        "Gender": "Male",
        "JobInvolvement": 1,
        "JobLevel": 2,
        "JobRole": "Sales Executive",
        "JobSatisfaction": 1,
        "MaritalStatus": "Single",
        "MonthlyIncome": 3000,
        "MonthlyRate": 15000,
        "NumCompaniesWorked": 5,
        "OverTime": "Yes",
        "PercentSalaryHike": 10,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": 2,
        "StockOptionLevel": 0,
        "TotalWorkingYears": 7,
        "TrainingTimesLastYear": 1,
        "WorkLifeBalance": 1,
        "YearsAtCompany": 2,
        "YearsInCurrentRole": 1,
        "YearsSinceLastPromotion": 0,
        "YearsWithCurrManager": 1
    }

    with patch("app.api.v1.endpoints.predictions.predict_probability") as mock_predict:
        mock_predict.return_value = 0.82

        response = client.post("/predict", json=test_input)

        assert response.status_code == 200
        assert response.json()["churn_probability"] == 0.82
        assert mock_predict.called
