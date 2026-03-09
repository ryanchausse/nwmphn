import os, json
from helper_functions import HelperFunctions
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

print("Starting...")
app = FastAPI()

# Define data model with Pydantic

# Example: root json response
@app.get("/")
def get_root():
    return {"Hello and welcome!"}

# Example: get request which returns a Jinja2 template with HTML

# Example: post request to create a new resource

# Example: put request to change a resource (all necessary fields)

# Example: patch request to change a resource (only fields that are changing)

print(HelperFunctions.test_function())
print("Done.")
