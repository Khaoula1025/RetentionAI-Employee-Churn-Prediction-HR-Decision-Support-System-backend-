from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from app.db.session import Base
class PredictionHistory(Base):
    __tablename__ = "predictions_history"

    id = Column(Integer, primary_key=True, index=True)  # auto-increment

    user_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),nullable=False
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False,
        unique=True   # 👈 enforces ONE prediction per employee
    )

    probability = Column(Float, nullable=False)

    # ORM relationships
    user = relationship("User", back_populates="predictions")
    employee = relationship("Employee", back_populates="prediction")
