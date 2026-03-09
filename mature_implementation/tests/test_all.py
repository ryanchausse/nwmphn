# Not doing this as the main dependency, the DB, is not created
# I could mock it, but this is meant to be just an exploratory repo

"""
In a mature state, sequence of events is:

Route registration of Thing route(main.py)
Instantiation of DB session (router/thing_router.py)
Instantiation of repo which uses DB session (repositories/thing_repository.py)
Instantiation of service which needs repo (services/thing_service.py)
Return by bubbling up DB query results (session -> repo -> service -> router)

Dependencies are:
main.py -> thing router
thing router -> FastAPI's Depends and APIRoter, db.session.get_db, schemas, repos, services
thing repo -> thing model
thing service -> thing repo, possibly other services
...
thing model -> SQLAlchemy ORM "Base" model and types
thing schema -> Pydantic BaseModel and types
...
db base -> sqlalchemy ORM declarative_base
db session -> sqlalchemy create_engine, SessionMaker

NB: repo handles transaction commits/flushing

Layers:
routes = HTTP request handling, auth, throttling
session = DB sessions (can connect to RDS proxy for example)
repo = data access layer via DB session which handles transactions
service = business logic (domain) layer, pretty fat

model is SQL table model, schema is Pydantic type model
"""