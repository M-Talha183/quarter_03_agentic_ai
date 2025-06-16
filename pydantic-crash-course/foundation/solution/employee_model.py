# from pydantic import BaseModel , Field # type: ignore
# from typing import Optional 

# class Employee(BaseModel):
#     id : int 
#     name : str = Field(
#         ...,
#         min_length =3, 
#         max_length =50, 
#         description ="Employee name", 
#         example ="Muhammad Talha",
#         )
    
#     department : Optional [str] = "General"
#     salary : float = Field(..., ge= 10000)
from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name",
        example="Muhammad Talha",
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)
