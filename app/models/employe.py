from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)  # auto-increment

    Age = Column(Integer, nullable=False)
    BusinessTravel = Column(String(50), nullable=False)
    DailyRate = Column(Integer, nullable=False)
    Department = Column(String(100), nullable=False)
    DistanceFromHome = Column(Integer, nullable=False)
    Education = Column(Integer, nullable=False)
    EducationField = Column(String(100), nullable=False)
    EnvironmentSatisfaction = Column(Integer, nullable=False)
    Gender = Column(String(20), nullable=False)
    JobInvolvement = Column(Integer, nullable=False)
    JobLevel = Column(Integer, nullable=False)
    JobRole = Column(String(100), nullable=False)
    JobSatisfaction = Column(Integer, nullable=False)
    MaritalStatus = Column(String(50), nullable=False)
    MonthlyIncome = Column(Integer, nullable=False)
    MonthlyRate = Column(Integer, nullable=False)
    NumCompaniesWorked = Column(Integer, nullable=False)
    OverTime = Column(String(10), nullable=False)
    PercentSalaryHike = Column(Integer, nullable=False)
    PerformanceRating = Column(Integer, nullable=False)
    RelationshipSatisfaction = Column(Integer, nullable=False)
    StockOptionLevel = Column(Integer, nullable=False)
    TotalWorkingYears = Column(Integer, nullable=False)
    WorkLifeBalance = Column(Integer, nullable=False)
    YearsAtCompany = Column(Integer, nullable=False)
    YearsInCurrentRole = Column(Integer, nullable=False)
    YearsSinceLastPromotion = Column(Integer, nullable=False)
    YearsWithCurrManager = Column(Integer, nullable=False)

    # Relation to predictions (1 employee → many predictions)
    prediction = relationship(
        "PredictionHistory",
        back_populates="employee",
        uselist=False
    )