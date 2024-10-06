# weather_model.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_storage.database_setup import WeatherData, Base

# Reusing the setup defined in `database_setup.py`
DATABASE_URL = "sqlite:///weather_data.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_weather_data(data):
    """Add new weather data to the database."""
    try:
        weather_entry = WeatherData(**data)
        session.add(weather_entry)
        session.commit()
        print("Weather data added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding weather data: {e}")

if __name__ == "__main__":
    # Example data entry
    data = {
        "temperature": 23.5,
        "humidity": 60.0,
        "wind_speed": 5.5,
        "datetime": "2024-10-06 12:00:00",
        "source": "NOAA"
    }
    add_weather_data(data)
