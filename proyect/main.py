from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import Response
from routes.route_company import router_company
from routes.route_country import router_country
from routes.route_language import router_language
from routes.route_auth import router_auth 
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi_jwt_auth import AuthJWT
from schemas.settings import Settings
from utils.utils import verify_login
# from routes.protected import protected_router #! ignorar
from db import create_tables

app = FastAPI()
auth = AuthJWT()

# app.include_router(protected_router) #! ignorar
app.include_router(router_auth)
app.include_router(router_company, dependencies=[Depends(verify_login(auth, "company"))])
app.include_router(router_language, dependencies=[Depends(verify_login("pepe"))]) 
app.include_router(router_country, dependencies=[Depends(verify_login("company"))])

create_tables()

@AuthJWT.load_config
def get_config():
  return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
  return JSONResponse(
    status_code=exc.status_code,
    content={"detail": exc.message}
  )
  
@app.get('/')
def home(user: str = Depends(verify_login)):
  return user
  
  

    