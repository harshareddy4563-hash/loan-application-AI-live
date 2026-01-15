from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base

class LoanApplication(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    applicant_aadhaar = Column(String)
    guardian_aadhaar = Column(String)

    applicant_face = Column(LargeBinary)
    guardian_face = Column(LargeBinary)

    cibil_score = Column(Integer)
    status = Column(String)
