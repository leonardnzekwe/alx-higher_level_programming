#!/usr/bin/python3
"""
relationship_state Module
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_city import City


Base = declarative_base()


class State(Base):
    """
    State class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', back_populates='state',
        cascade='all, delete-orphan'
    )
