from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
import csv

app = FastAPI()

# Ran out of time to add the various constraints (a la [constr(max_length=256)])
class ClientModel(BaseModel):
    id: int
    client_key: str # This should be uuid.uuid4
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
# Add one test client (me)
my_client = ClientModel(
    id=1,
    client_key=str(uuid.uuid4()),
    slk="LKE102310",
    forename="Ryan",
    family_name="Chausse",
    date_of_birth="1986-01-01",
    intersex=1,
    phone="0418759273"
)
example_clients: list[ClientModel] = [my_client,]

with open('./client_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            example_clients.append(
                ClientModel(
                    id=row["id"],
                    client_key=row["client_key"],
                    slk=row["slk"],
                    forename=row["forename"],
                    preferred_forename=row["preferred_forename"],
                    family_name=row["family_name"],
                    pronoun=row["pronoun"],
                    date_of_birth=row["date_of_birth"],
                    gender=row["gender"],
                    intersex=row["intersex"],
                    sexual_orientation=row["sexual_orientation"],
                    indigenous_status=row["indigenous_status"],
                    country_of_birth=row["country_of_birth"],
                    main_lang_at_home=row["main_lang_at_home"],
                    phone=row["phone"],
                    email=row["email"],
                    suburb=row["suburb"],
                    state=row["state"],
                    postcode=row["postcode"],
                    consent_email=row["consent_email"],
                    consent_sms=row["consent_sms"],
                )
            )
        except (ValueError, TypeError) as e:
            print(f"There was an error parsing the CSV row into a ClientModel object: {e}")
        except Exception as e:
            print(f"Unforeseen error parsing CSV row: {e}")
        finally:
            print(f"Row data: {row}")
            print("Row skipped.")
            pass

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
) -> list[ClientOutModel]:
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
