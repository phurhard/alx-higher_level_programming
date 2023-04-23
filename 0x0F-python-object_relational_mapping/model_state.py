#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
"""Class definition of a state and an instance of Base = declarative_base()"""

Base = declarative_base()

class State(Base):
    """The State class that defines some of the requirements needed for working with sqlalchemy"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
