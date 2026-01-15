from fastapi import FastAPI, UploadFile, File, Form
from database import engine, SessionLocal
from models import Base, LoanApplication
from face_utils import get_face_encoding, verify_faces

Base.metadata.create_all(bind=engine)
app = FastAPI()

CIBIL_THRESHOLD = 780

@app.post("/apply-loan")
async def apply_loan(
    applicant_aadhaar: str = Form(...),
    guardian_aadhaar: str = Form(...),
    cibil_score: int = Form(...),
    applicant_face: UploadFile = File(...),
    guardian_face: UploadFile = File(...)
):
    db = SessionLocal()

    app_img = await applicant_face.read()
    guard_img = await guardian_face.read()

    app_enc = get_face_encoding(app_img)
    guard_enc = get_face_encoding(guard_img)

    if app_enc is None or guard_enc is None:
        status = "Rejected - Face not detected"
    elif not verify_faces(app_enc, guard_enc):
        status = "Rejected - Same person"
    elif cibil_score < CIBIL_THRESHOLD:
        status = "Rejected - Low CIBIL"
    else:
        status = "Approved"

    loan = LoanApplication(
        applicant_aadhaar=applicant_aadhaar,
        guardian_aadhaar=guardian_aadhaar,
        applicant_face=app_img,
        guardian_face=guard_img,
        cibil_score=cibil_score,
        status=status
    )

    db.add(loan)
    db.commit()

    return {"status": status}
