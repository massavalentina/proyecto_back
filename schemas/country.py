from pydantic import BaseModel, Field

###########################################################################################*
#*                                        SCHEMAS                                         #
###########################################################################################* 


class CountryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    

class Country(CountryCreate):
    id: int

    class Config:
        orm_mode: True