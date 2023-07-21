from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db import get_db
from schemas.company import CompanyCreate, Company
from models.company import CompanyModel



###########################################################################################*
#*                                        ROUTES                                          #
###########################################################################################*

router_company = SQLAlchemyCRUDRouter(
  schema=Company,
  create_schema=CompanyCreate,
  db_model= CompanyModel,
  db= get_db,
  prefix='company'
)
