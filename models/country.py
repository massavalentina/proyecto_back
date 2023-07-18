from db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


###########################################################################################*
#*                                        MODELS                                          #
###########################################################################################*

class CountryModel(Base):
    __tablename__ = 'Countries'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))


# id
# nombre
