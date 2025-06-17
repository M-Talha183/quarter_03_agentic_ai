from pydantic import BaseModel
from typing import List
from datetime import datetime 


class Adress(BaseModel):
    street : int
    city : str
    zip_code : str
    
class User(BaseModel):
    id : int 
    name : str 
    email : str 
    is_active : bool = True
    createdAt : datetime
    address : Adress
    tags : List[str] = []
    
    
user= User(
    id = 1,
    name = "Talha",
    email = "abc@gmail.com",
    createdAt = datetime(2024,3,15,14,10),
    address = Adress(
        street =123,
        city="Karachi",
        zip_code="00114455"
    ),
    is_active=False,
    tags=["premmium","subscriber"],
    
)

#  using model_dump() -> dict 
python_dict = user.model_dump()
print(python_dict) 

#  using model_dump() -->  json
json_str = user.model_dump_json()
print(json_str)