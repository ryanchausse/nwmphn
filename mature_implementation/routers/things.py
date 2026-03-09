from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from mature_implementation.db.session import get_db
from mature_implementation.schemas import Thing, ThingResponse
from mature_implementation.repositories import ThingRepository
from mature_implementation.services import ThingService

router = APIRouter.add_route(prefix="/things")

@router.get("/", response_model=ThingResponse)
def get_thing(thing_id: int, db: Session = Depends(get_db)):
    # Register repository (data access layer) and inject into service (domain layer)
    repo = ThingRepository(db)
    service = ThingService(repo)
    return service.get_thing(thing_id)
