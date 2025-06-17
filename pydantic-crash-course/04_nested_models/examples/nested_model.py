from typing import List , Optional
from pydantic import BaseModel


class Address(BaseModel):
    street : str 
    city : str 
    postal_code : str 
    

class User (BaseModel):
    id : int 
    name : str 
    address : Address  
    
    
class Comment (BaseModel):
    id : int 
    content : str 
    replies : Optional[List['Comment']] = None 
    
    
Comment.model_rebuild()


adress = Address(
    street= "123 Some Thing",
    city = "Karachi",
    postal_code= "10023"
)
user = User(
    id= 101,
    name= "Muhammad Talha",
    address= adress
)


comment = Comment(
    id = 1,
    content= "First Comment ",
    replies= [
        Comment(id=2,content = "reply2"),
        Comment(id=3,content = "reply3"),
        ]
)