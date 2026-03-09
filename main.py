import os, json
from datetime import datetime
from helper_functions import HelperFunctions
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Template
from pydantic import BaseModel
from typing import Optional

load_dotenv()

print("Starting...")
app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Define data model with Pydantic
# TODO: make "id" and "created_at" automatically generated in POST route
class Thing(BaseModel):
    id: int
    name: str
    created_at: datetime
    price: Optional[float] = None
    description: Optional[str] = None
    is_true: Optional[bool] = None
    updated_at: Optional[datetime] = None


# Define response (minimised / sanitised) model for Thing
# TODO: review sanitisation for output object
class ThingOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# Initialise one thing in a thing list (later I'll put this in SQLite or equivalent)
# Consider using a set() here instead if id will never be a duplicate (might not be
# an issue if constraints are in the DB)
example_things: list[Thing] = [Thing(
    id = 0,
    name = "Example Thing",
    price = 13.99,
    created_at = datetime.now()
),]

# Example: root json response
@app.get("/")
def get_root():
    return "Hello and welcome!"

# Example: find things matching search criteria or list all things
# TODO: paginate (page/page size or offset/limit)
# TODO: decide whether to derive searchable fields from enum or to 
#       define them in each route (whitelist might make the code more
#       succinct but be vulnerable to oversight / misuse / scale issues)
# TODO: return results that are LIKE, not equal to, the query params
@app.get("/things")
def find_things(
    id: int | None = None,
    name: str | None = None,
    description: str | None = None,
    created_at: datetime | None = None
):
    if all(arg is None for arg in (id, name, description, created_at)):
        return example_things

    return [
        x for x in example_things
        # TODO: fix usage bug where user can supply wrong filtering values
        #       e.g. correct name and unmatched/wrong id for a single object
        if (
            id is not None and x.id == id or
            name is not None and x.name == name or
            description is not None and x.description == description or
            created_at is not None and x.created_at == created_at
        )
    ]

# Example: GET request for a particular "Thing" object/item
@app.get("/thing/{thing_id}")
def get_thing(thing_id: int):
    search_result = [x for x in example_things if x.id == thing_id]
    if not search_result:
        return HTTPException(status_code=404, detail="Thing not found")
    if len(search_result) > 1:
        return HTTPException(status_code=500, detail="More than one Thing found")
    return {
        "id": search_result[0].id,
        "name": search_result[0].name,
        "created_at": search_result[0].created_at
    }

# Example: get request which returns a Jinja2 template with HTML
# TODO: apply as an optional argument to the normal "/things" route
@app.get("/things_html", response_class=HTMLResponse)
def find_things_html(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="base.html",
        context={"things": example_things}
    )

# Example: POST request to create a new resource (Thing)
@app.post("/things", response_model=ThingOut, status_code=201)
def create_thing(thing: Thing):
    example_things.append(thing)
    return thing

# Example: put request to change a resource (all necessary fields)
@app.put("/things/{thing_id}", response_model=ThingOut, status_code=200)
def replace_thing(thing_id: int, thing: Thing):
    for existing_thing in example_things:
        if (existing_thing.id == thing_id):
            example_things.remove(existing_thing)
            example_things.append(thing)


# Example: patch request to change a resource (only fields that are changing)

print("Done.")
