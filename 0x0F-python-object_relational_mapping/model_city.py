#!/usr/bin/python3
"""This contains the City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """This class is the City class
    Args:
        Base: inheriting from Base class
    Attributes:
        id: id of the City
        name: name of the City
        state_id: the id of the state
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
