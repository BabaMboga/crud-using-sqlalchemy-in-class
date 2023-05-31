from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///dogs.db')  
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define the Dog class
class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    
    def create(name, breed, age):
        dog = Dog(name, breed, age)
        session.add(dog)
        session.commit()
        return dog

    
    def read_all():
        return session.query(Dog).all()

   
    def read_by_id(dog_id):
        return session.query(Dog).filter(Dog.id == dog_id).first()

    def update(self, name=None, breed=None, age=None):
        if name:
            self.name = name
        if breed:
            self.breed = breed
        if age:
            self.age = age
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

#Create the table
Base.metadata.create_all(engine)

# Create a new dog
dog1 = Dog.create('Buddy', 'Labrador', 5)
dog2 = Dog.create('Ric', 'Mastiff', 2)
dog3 = Dog.create('', 'Mastiff', 2)
dog4 = Dog.create('Ric', 'Mastiff', 2)

# Fetch all dogs
all_dogs = Dog.read_all()
for dog in all_dogs:
    print(dog.name, dog.breed, dog.age)

# Update a dog
# dog1.update(name='Buddy Jr.', age=6)

# Delete a dog
# dog1.delete()


