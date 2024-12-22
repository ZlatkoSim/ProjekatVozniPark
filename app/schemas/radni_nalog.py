from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from schemas.vozac import VozacOut
from schemas.vozilo import VoziloOut

class StatusRadnogNalogaEnum(str, Enum):
    otvoren = 'otvoren'
    u_toku = 'u toku'
    zavrsen = 'zavrsen'

class RadniNalogBase(BaseModel):
    vozilo_id: int
    vozac_id: int
    opis_zadatka: str
    datum_i_vrijeme_izdavanja: datetime
    rok_zavrsavanja: datetime
    status: StatusRadnogNalogaEnum
    vozilo: VoziloOut  
    vozac: VozacOut 

class RadniNalogCreate(BaseModel):
    vozilo_id: int
    vozac_id: int
    opis_zadatka: str
    datum_i_vrijeme_izdavanja: datetime
    rok_zavrsavanja: datetime
    status: StatusRadnogNalogaEnum

class RadniNalogOut(RadniNalogBase):
    id: int
    
    class Config:
       from_attributes = True
