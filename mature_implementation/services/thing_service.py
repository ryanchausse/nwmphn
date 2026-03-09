from mature_implementation.repositories.thing_repository import ThingRepository

class ThingService:
    def __init__(self, repo: ThingRepository):
        self.repo = repo

    def get_thing(self, thing_id: int):
        # TODO: put checks in here for things like null handling
        return self.repo.get_thing(thing_id)
