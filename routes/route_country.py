from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from schemas.country import CountryCreate, Country
from models.country import CountryModel


###########################################################################################*
#*                                        ROUTES                                          #
###########################################################################################*


router_country = SQLAlchemyCRUDRouter(
    schema=Country,
    create_schema=CountryCreate,
    db_model= CountryModel,
    db= get_db,
    prefix='company'
)
