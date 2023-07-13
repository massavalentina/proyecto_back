from pydantic import BaseModel, Field
import re   


###########################################################################################*
#*                                        SCHEMAS                                         #
###########################################################################################*                                                


class CompanyCreate(BaseModel):
    name: str = Field(gt=3, lt=50  )
    web_direction: str = Field(regex='^((www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$')
    web_direction2: str = Field(regex= '^(www\.)*[A-Za-z0-9_-]+\.[A-Za-z]{2,}$')


class Company(CompanyCreate):
    id: int

    class Config:
        orm_mode: True