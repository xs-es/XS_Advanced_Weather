# database_setup.py
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class WeatherData(Base):
    """SQLAlchemy ORM model for storing weather data."""
    __tablename__ = 'weather_data'
    
    id = Column(Integer, primary_key=True)
    temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    datetime = Column(DateTime)
    source = Column(String)

# Database setup
DATABASE_URL = "sqlite:///weather_data.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def initialize_database():
    """Initialize the database by creating tables."""
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")
