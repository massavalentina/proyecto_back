from pydantic import BaseModel, Field
import re   


###########################################################################################*
#*                                        SCHEMAS                                         #
###########################################################################################*                                                


class CompanyCreate(BaseModel):
    name: str = Field(gt=3, lt=50  )
    web_direction: str = Field(regex=r"^(https?:\/\/)?(www\.)?\w+\.\w+(\.\w+)?$")
    


class Company(CompanyCreate):
    id: int

    class Config:
        orm_mode = True

        