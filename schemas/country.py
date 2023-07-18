from pydantic import BaseModel, Field

###########################################################################################*
#*                                        SCHEMAS                                         #
###########################################################################################* 


class CountryCreate(BaseModel):
    name: str = Field(gt=2, lt=50)
    

class Country(CountryCreate):
    id: int

    class Config:
        orm_mode = True