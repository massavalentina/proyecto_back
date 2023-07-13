from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from schemas.language import LanguageCreate, Language
from models.language import LanguageModel


###########################################################################################*
#*                                        ROUTES                                          #
###########################################################################################*


router_language = SQLAlchemyCRUDRouter(
    schema=Language,
    create_schema=LanguageCreate,
    db_model= LanguageModel,
    db= get_db,
    prefix='company'
)
