# # part one 
from pydantic import BaseModel

from typing import List , Dict , Optional  

# class Users(BaseModel):
#     id : int 
#     name : str 
#     is_active : bool 
    
# user_input = {"id":101, "name": "Talha", "is_active":True}

# u1 = Users(**user_input)
# print(u1)

# ************** ****************** Part 02 ****************************************************************

class Cart (BaseModel) :
    user_id : int 
    items : List[str]
    quantities : Dict[str, int ]
    
class BlogPost (BaseModel) : 
    title : str
    content : str 
    image_url : Optional[str] =  None
    