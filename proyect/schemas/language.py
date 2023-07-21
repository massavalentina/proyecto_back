from pydantic import BaseModel, Field


###########################################################################################*
#*                                        SCHEMAS                                         #
###########################################################################################* 


class LanguageCreate(BaseModel):
  name: str = Field(min_length=2, max_length=50)
    

class Language(LanguageCreate):
  id: int

  class Config:
    orm_mode = True

