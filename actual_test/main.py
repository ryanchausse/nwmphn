from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
import csv

app = FastAPI()

# Ran out of time to add the various constraints a la [constr(max_length=256)]
class ClientModel(BaseModel):
    id: int
    client_key: uuid.uuid4
    slk: str
    forename: str
    preferred_forename: Optional[str] = None # This name differs in the model spec
    family_name: str
    pronoun: str | None = None # This can be an enum or str, may include int
    date_of_birth: datetime
    gender: str | None = None
    intersex: int # This is an enum
    sexual_orientation: str | None = None
    indigenous_status: str | None = None
    country_of_birth: str | None = None
    main_lang_at_home: str | None = None
    phone: str
    email: EmailStr | None = None
    suburb: str | None = None
    state: str | None = None # Prob. an enum here
    postcode: str | None = None # The example was text; I know Canadian post codes can contain letters, so, keeping strings
    consent_mail: bool = False
    consent_email: bool = False
    consent_voice_message: bool = False
    consent_sms: bool = False


# Define response (minimised / sanitised) model for Client
class ClientOutModel(BaseModel):
    id: int
    family_name: str
    forename: str
    preferred_forename: Optional[str] = None
    phone: str


# Read provided sample data into ClientModel(s) and append to list
example_clients: list[ClientModel] = []

with open('./client_data.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        try:
            example_clients.append(
                ClientModel(
                    id=row[0],
                    client_key=row[1],
                    slk=row[2],
                    forename=row[3],
                    preferred_forename=row[4],
                    family_name=row[5],
                    pronoun=row[6],
                    date_of_birth=row[7],
                    gender=row[8],
                    intersex=row[9],
                    sexual_orientation=row[10],
                    indigenous_status=row[11],
                    country_of_birth=row[12],
                    main_lang_at_home=row[13],
                    phone=row[14],
                    email=row[15],
                    suburb=row[16],
                    state=row[17],
                    postcode=row[18],
                    consent_mail=row[19],
                    consent_email=row[20],
                    consent_voice_message=row[21],
                    consent_sms=row[22],
                )
            )
        except (TypeError, ValueError) as e:
            # Only notify and continue parsing
            print("There was a problem parsing a row")
            print(f"Error message: {e}")
            print(f"Row data: {row}")


# Example: root json response
@app.get("/")
def get_root():
    return "Please see available API documentation at <a href='./docs'>the documentation page</a>."

@app.get("/clients")
def find_clients(
    id: int | None = None,
    forename: str | None = None,
    family_name: str | None = None,
    date_of_birth: datetime | None = None
) -> list[ClientOutModel]: # Using ClientModel arbitrarily here
    if all(arg is None for arg in (id, forename, family_name, date_of_birth)):
        return example_clients # Likely needs pagination

    return [
        x for x in example_clients
        # TODO: fix usage bug where user can supply wrong filtering values
        #       e.g. correct name and unmatched/wrong id for a single object
        if (
            (id is not None and x.id == id) or
            (forename is not None and x.forename == forename) or
            (family_name is not None and x.family_name == family_name) or
            (date_of_birth is not None and x.date_of_birth == date_of_birth)
        )
    ]

# Example: GET request for a particular Client object/item
@app.get("/clients/{client_id}", response_model=ClientOutModel)
def get_client(client_id: int):
    search_result = [x for x in example_clients if x.id == client_id]
    if not search_result:
        raise HTTPException(status_code=404, detail="Client not found")
    if len(search_result) > 1:
        raise HTTPException(status_code=500, detail="More than one Client found")
    return search_result[0]

# Example: POST request to create a new resource (Client)
@app.post("/clients", response_model=ClientOutModel, status_code=201)
def create_thing(client: ClientModel):
    example_clients.append(client)
    return client
