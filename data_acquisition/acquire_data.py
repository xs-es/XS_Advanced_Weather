# acquire_data.py
from data_acquisition.sources.noaa_api import get_noaa_data
from data_acquisition.sources.vdatum_api import get_vdatum_data

def acquire_weather_data():
    """Acquire data from multiple sources and return the combined dataset."""
    print("Fetching NOAA data...")
    noaa_data = get_noaa_data()

    print("Fetching VDatum data...")
    vdatum_data = get_vdatum_data()

    # For now, just combining both datasets as a list (could be more sophisticated in future)
    combined_data = {
        'noaa': noaa_data,
        'vdatum': vdatum_data
    }

    return combined_data
