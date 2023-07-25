from db import Base
from sqlalchemy import Column, Integer, String


###########################################################################################*
#*                                        MODELS                                          #
###########################################################################################*

class CountryModel(Base):
  __tablename__ = 'countries'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100))


# id
# nombre
