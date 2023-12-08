#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
Session=sessionmaker()
# Base.metadata.create_all(engine)
    

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
    
    def __repr__(self):
        return f"{self.id} {self.name} {self.breed}"



    