from pydantic import BaseModel

class Restaurant(BaseModel):
    name:str
    
class Item(BaseModel):
    name:str
    cost:int