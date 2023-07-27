from fastapi import Depends, HTTPException
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from models.user import UserModel
from schemas.language import LanguageCreate, Language
from models.language import LanguageModel
from sqlalchemy.orm.session import Session


###########################################################################################*
#*                                        ROUTES                                          #
###########################################################################################*


router_language = SQLAlchemyCRUDRouter(
  schema=Language,
  create_schema=LanguageCreate,
  db_model= LanguageModel,
  db= get_db,
  prefix='language',
  delete_one_route=False
)



@router_language.delete('/{id}')
def delete_one_route(id: int, db: Session = Depends(get_db)):
  user = db.query(UserModel).filter_by(usr_language = id).first()
  if user:
    raise HTTPException(status_code=400, detail='No se puede eliminar el lenguaje porque esta siendo usado por un usuario')
  
  language = db.query(LanguageModel).filter_by(id = id).first()
  db.delete(language)
  db.commit()
  