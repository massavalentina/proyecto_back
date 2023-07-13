from pydantic import BaseModel, Field


###########################################################################################*
#*                                        SCHEMAS                                         #
###########################################################################################* 


class LanguageCreate(BaseModel):
    name: str = Field(gt=2, lt=50 )
    

class Language(LanguageCreate):
    id: int

    class Config:
        orm_mode: True

