from datetime import datetime
from typing import Union

from model import Base, Visit
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship


class Property(Base):
    __tablename__ = 'properties'

    id = Column("pk_property", Integer, primary_key=True)
    title = Column(String(250), unique=True)
    address = Column(String(150))
    value = Column(Float)
    size = Column(Float)
    rooms = Column(Integer)
    bathrooms = Column(Integer)
    garages = Column(Integer)
    type = Column(String(100))
    thumbnail = Column(String(500))
    
    visits = relationship("Visit")

    created_at = Column(DateTime, default=datetime.now())

    def __init__(
        self,
        title:str,
        address:str,
        value:float,
        size: float,
        rooms: int,
        bathrooms: int,
        garages: int,
        type: str,
        thumbnail: str,
        created_at:Union[DateTime, None] = None
    ):
        """
        Creata a Property

        Arguments:
            title: property title to show in app
            address: property location
            value: property value
            size: property size
            rooms: property rooms
            bathrooms: property bathrooms
            bathgaragesrooms: property garages
            created_at: created date in database
        """
        self.title = title
        self.address = address
        self.value = value
        self.size = size
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.garages = garages
        self.type = type
        self.thumbnail = thumbnail

        # se não for informada, será o data exata da inserção no banco
        if created_at:
            self.created_at = created_at
    
    def add_visit(self, visit:Visit):
        """ Adiciona uma nova visita à Propriedade
        """
        self.visits.append(visit)
