from fastapi import FastAPI
from routes.user_route import router_user
from routes.book_route import router_book
from routes.state_route import router_state
from routes.country_route import router_country
from routes.especial_route import router_especial

from db import create_tables


app = FastAPI()

create_tables()


