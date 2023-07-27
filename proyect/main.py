# from routes.protected import protected_router #! ignorar
from db import create_tables
from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse, Response
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from routes.route_auth import router_auth
from routes.route_company import router_company
from routes.route_country import router_country
from routes.route_language import router_language
from schemas.settings import Settings
from utils.utils import verify_login

app = FastAPI()
auth = AuthJWT()

# app.include_router(protected_router) #! ignorar
app.include_router(router_auth, dependencies=[Depends(verify_login(auth,"Auth"))])
app.include_router(router_company,dependencies=[Depends(verify_login("Company"))])
app.include_router(router_language,dependencies=[Depends(verify_login("Language"))])
app.include_router(router_country,dependencies=[Depends(verify_login("Country"))])

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

    