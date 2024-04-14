#!/usr/bin/python3
"""This module houses a definition of State class, which
is mapped to a database table through the ORM"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class defines a state's properties, such as id with state
    name and maps these properties to a database table."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
