from db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


###########################################################################################*
#*                                        MODELS                                          #
###########################################################################################*  


class CompanyModel(Base):
  __tablename__ = 'Companies'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100))
  web_direction = Column(String(100))
    
# id
# nombre min 2 max 50
# direccion_web direc web valida (www.nombre.com.ar o sin el www)

# min 3 max 50


