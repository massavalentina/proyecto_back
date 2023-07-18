from db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


###########################################################################################*
#*                                        MODELS                                          #
###########################################################################################*

class LanguageModel(Base):
    __tablename__ = 'Language'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    

# id
# nombre
# min 2 caracteres maximo 50
