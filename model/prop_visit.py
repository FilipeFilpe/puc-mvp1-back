from datetime import datetime
from typing import Union

from model import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String


class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    email = Column(String(150))
    phone = Column(String(150))
    date = Column(String(150))
    property = Column(Integer, ForeignKey("properties.pk_property"), nullable=False)

    created_at = Column(DateTime, default=datetime.now())

    def __init__(
        self,
        name:str,
        email:str,
        phone:str,
        date:str,
        created_at:Union[DateTime, None] = None
    ):
        """
        Create a Visit

        Arguments:
            name: visit name
            email: visit email
            phone: visit phone
            date: visit date
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.date = date

        # se não for informada, será o data exata da inserção no banco
        if created_at:
            self.created_at = created_at
