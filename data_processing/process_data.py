# process_data.py
import pandas as pd

def process_weather_data(raw_data):
    """Process raw weather data from different sources."""
    try:
        # Example: Converting NOAA data to a DataFrame
        noaa_data = raw_data.get('noaa', {}).get('properties', {}).get('periods', [])
        df_noaa = pd.DataFrame(noaa_data)

        # Example: Process VDatum data (as dictionary for now)
        vdatum_data = raw_data.get('vdatum', {})

        # Return processed data as needed
        return {
            'noaa_df': df_noaa,
            'vdatum': vdatum_data
        }
    except Exception as e:
        print(f"Error processing data: {e}")
        return {}
