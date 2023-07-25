from pydantic import BaseModel, Field
# import re   


###########################################################################################*
#*                                        SCHEMAS                                         #
###########################################################################################*                                                


class CompanyCreate(BaseModel):
  name: str = Field(min_length=3, max_length=50)
  web_direction: str = Field(regex=r"^(https?://)?(www\.)?[\w-]+\.(com|net|org|app|io)$")


class Company(CompanyCreate):
  id: int

  class Config:
      orm_mode = True