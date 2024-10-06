# noaa_api.py
import requests

def get_noaa_data():
    """Fetch data from NOAA API."""
    try:
        response = requests.get("https://api.weather.gov/gridpoints/TOP/31,80/forecast")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NOAA data: {e}")
        return {}
