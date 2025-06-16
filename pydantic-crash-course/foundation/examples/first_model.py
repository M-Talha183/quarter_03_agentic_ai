from pydantic import BaseModel 

class Users(BaseModel):
    id : int 
    name : str 
    is_active : bool 
    
user_input = {"id":101, "name": "Talha", "is_active":True}

u1 = Users(**user_input)
print(u1)