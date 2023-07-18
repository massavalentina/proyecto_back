from fastapi import FastAPI
from pydantic import BaseSettings
from datetime import timedelta
from routes.route_company import router_company
from routes.route_country import router_country
from routes.route_language import router_language

from db import create_tables

app = FastAPI()

app.include_router(router_company)
app.include_router(router_language)
app.include_router(router_country)
# app.include_router()

create_tables()

class Settings(BaseSettings):
    pass

    