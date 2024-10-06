# vdatum_api.py
import requests

def get_vdatum_data():
    """Fetch elevation and geodetic data from the VDatum API."""
    try:
        url = "https://vdatum.noaa.gov/vdatumweb/api/convert?s_x=-75.211&s_y=36.129"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching VDatum data: {e}")
        return {}
