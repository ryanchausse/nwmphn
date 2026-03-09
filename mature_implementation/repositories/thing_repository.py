from mature_implementation.models import Thing
from sqlalchemy.orm import Session

class ThingRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_thing(self, thing_id: int):
        thing = self.db.query(Thing).filter(Thing.id == thing_id).first()
        return thing
