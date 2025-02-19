class Player:
    name: str
    skill_level: int #probably enum?
    wealth: int

class Inventory:
    items: dict
    materials: dict
    
class Work(abc): #this is not right
    id: int
    name: str
    quality: int #enum?
    value: int