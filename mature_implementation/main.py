from fastapi import FastAPI
from .routers import things

app = FastAPI()
app.include_router(things.router)
