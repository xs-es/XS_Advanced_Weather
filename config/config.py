# config.py
import os

class Config:
    """Application configuration settings."""
    
    # Flask settings
    DEBUG = os.getenv('DEBUG', True)
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')

    # Database settings
    DATABASE_URL = os.getenv('DATABASE_URL', "sqlite:///weather_data.db")

    # Twilio API settings
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', 'your_account_sid_here')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', 'your_auth_token_here')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', '+1234567890')

    # NOAA API settings (example)
    NOAA_API_URL = os.getenv('NOAA_API_URL', 'https://api.weather.gov/gridpoints/TOP/31,80/forecast')

    # VDatum API settings (example)
    VDATUM_API_URL = os.getenv('VDATUM_API_URL', 'https://vdatum.noaa.gov/vdatumweb/api/convert')

# Example usage in application
if __name__ == "__main__":
    print(f"Database URL: {Config.DATABASE_URL}")
