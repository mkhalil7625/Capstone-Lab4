from dataclasses import dataclass,field

NO_ID = -1

@dataclass
class Record:

    name:str
    country:str
    number:int
    id:int = NO_ID
