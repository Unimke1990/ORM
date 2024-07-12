from sqlalchemy import create_engine, Column, Integer, String, CHAR
from sqlalchemy.orm import declarative_base

# Create an engine that stores data in the local directory's mydb.db file.
engine = create_engine("sqlite:///database.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

# Define the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Define the string representation of the object
    def __str__(self):
        return f"User(name='{self.name}', age='{self.age}')"
    
    def __repr__(self):
        return self.__str__()
    
# Define columns
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create all tables in the engine
Base.metadata.create_all(engine)