from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.session import get_db


router = APIRouter()


@router.get("/")
def health_check():
    return {"status": "ok"}


@router.get("/db-check")
def database_check(
    db: Session = Depends(get_db)
):

    return {
        "database": "connected"
    }