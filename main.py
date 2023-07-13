from fastapi import FastAPI
from pydantic import BaseSettings
from datetime import timedelta

from db import create_tables

app = FastAPI()

app.include_router()
app.include_router()
app.include_router()
app.include_router()

create_tables()

class Settings(BaseSettings):
    pass

    