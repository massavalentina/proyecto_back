from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from models.user import UserModel
from utils.utils import create_user, verify_usr_email, authenticate_user
from schemas.user import UserCreate, UserLogin
from db import get_db
from sqlalchemy.orm.session import Session
from pydantic.typing import Annotated
from fastapi_jwt_auth.exceptions import AuthJWTException



router_auth = APIRouter(
  tags=['Authentication'],
  prefix='/auth'
)

#*################### AUTHENTICATION ######################
#*        Ruta para autenticar usuario                    #
#*#########################################################

db_dependency = Annotated[ Session, Depends(get_db)]

@router_auth.post('/register')
async def register( user: UserCreate, db: db_dependency ):
  await create_user(db, user)
  return 'ok'

@router_auth.get('/verify_email/{token}')
def verify( token: str, usr_email:str, db: db_dependency):
  verify_usr_email(token, usr_email, db)
  return 'ok'

@router_auth.post('/login')
def login( user: UserLogin, db: db_dependency, Authorize: AuthJWT = Depends() ):
  
  user_db = authenticate_user(user, db)
  
  access_token = Authorize.create_access_token(subject=user_db.usr_id)
  refresh_token = Authorize.create_refresh_token(subject=user_db.usr_id)
  
  Authorize.set_access_cookies(access_token)
  Authorize.set_refresh_cookies(refresh_token)
  return 'login exitoso'

@router_auth.delete('/logout')
def logout(Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  Authorize.unset_jwt_cookies()
  return {"msg":"Successfully logout"}





