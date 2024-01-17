from app.dal.models.base_model import Base

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Boolean, 
    Date
)

class ServisoKatalogas(Base):
    __tablename__ = 'serviso_katalogas'
    __metadata__ = Base.metadata

    id = Column(Integer, primary_key=True)
    paslaugos_kodas = Column(String, primary_key=True)
    institucijos_kodas = Column(Integer)
    institucijos_pavadinimas = Column(String)
    paslaugos_pavadinimas = Column(String)
    paslaugos_tipas = Column(String)
    el_paslauga = Column(String)
    tik_notarinis = Column(Boolean)
    prokuratura = Column(Boolean)
    aktyvumas = Column(Boolean)
    galioja_nuo = Column(Date)
    galioja_iki = Column(Date)

    def dict(self):
        return {
            "id": self.id,
            "paslaugos_kodas": self.paslaugos_kodas,
            "institucijos_kodas": self.institucijos_kodas,
            "institucijos_pavadinimas": self.institucijos_pavadinimas,
            "paslaugos_pavadinimas": self.paslaugos_pavadinimas,
            "paslaugos_tipas": self.paslaugos_tipas,
            "el_paslauga": self.el_paslauga,
            "tik_notarinis": self.tik_notarinis,
            "prokuratura": self.prokuratura,
            "aktyvumas": self.aktyvumas,
            "galioja_nuo": self.galioja_nuo,
            "galioja_iki": self.galioja_iki
        }