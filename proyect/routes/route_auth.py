from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from sqlalchemy import update
# from main import authjwt_exception_handler
from models.user import UserModel
from schemas.user import UserCreate, UserLogin
from db import get_db
from sqlalchemy.orm.session import Session
from pydantic.typing import Annotated
from fastapi_jwt_auth.exceptions import AuthJWTException
from utils.utils import get_password_hash, send_email

router_auth = APIRouter(
  tags=['Authentication'],
  prefix='/auth'
)

db_dependency = Annotated[ Session, Depends(get_db)]

@router_auth.post('/register')
async def register( user: UserCreate, db: db_dependency, Authorize: AuthJWT = Depends() ):
  usr_email = db.query(UserModel).filter_by(usr_email=user.usr_email).first() 

  if usr_email:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail="Email registrado"
    )

  hashed_password = get_password_hash(user.usr_password)

  user.usr_password = hashed_password
  db_user = UserModel(**user.dict())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  
  access_token = Authorize.create_access_token(subject=db_user.usr_id)
  Authorize.set_access_cookies(access_token)
  await send_email(access_token, user.usr_email)
  return 'ok'


@router_auth.get('/verify_email')
def verify( db: db_dependency, Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  try:
    usr_id = Authorize.get_jwt_subject()
     
    if not usr_id:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuario no autorizado gcu",
      )
      
    user_db = db.query(UserModel).filter_by(usr_id=usr_id).first()
    
    if not user_db:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
      )
    
    user_update = ( update(UserModel).where(UserModel.usr_id == usr_id).values(usr_enabled=True) )
    db.execute(user_update)
    db.commit()
    return 'ok'
  
  except AuthJWTException:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Token expirado",
    )


@router_auth.post('/login')
def login( user: UserLogin, db: db_dependency, Authorize: AuthJWT = Depends() ):
  
  user = db.query(UserModel).filter_by(usr_email=user.usr_email).first()
  
  if not user:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
  
  access_token = Authorize.create_access_token(subject=user.usr_id)
  refresh_token = Authorize.create_refresh_token(subject=user.usr_id)
  
  Authorize.set_access_cookies(access_token)
  Authorize.set_refresh_cookies(refresh_token)
  return 'login exitoso'


@router_auth.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):

  Authorize.jwt_refresh_token_required()

  current_user = Authorize.get_jwt_subject()
  new_access_token = Authorize.create_access_token(subject=current_user)
  Authorize.set_access_cookies(new_access_token)

@router_auth.delete('/logout')
def logout(Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  Authorize.unset_jwt_cookies()
  return {"msg":"Successfully logout"}







