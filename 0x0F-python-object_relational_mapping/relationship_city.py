#!/usr/bin/python3
"""This module houses the definition of a model to create a mapped
class whose attributes or properties are used to form a db table
to store a cities data."""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """This is mapped class definition whose
    properties are used to create a db table"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
