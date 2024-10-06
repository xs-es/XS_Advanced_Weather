# analyze_data.py
import pandas as pd
from sklearn.linear_model import LinearRegression

def perform_analysis(data):
    """Perform analysis on weather data."""
    try:
        # Example: Using NOAA DataFrame to predict future temperature
        df = data.get('noaa_df')
        
        if df is not None:
            # Simple example: Predict temperature based on period (time)
            df['period'] = df.index
            X = df[['period']].values.reshape(-1, 1)
            y = df['temperature'].values.reshape(-1, 1)

            model = LinearRegression()
            model.fit(X, y)

            print("Linear Regression model trained for temperature prediction.")
            return {
                "model": model,
                "data": df
            }
    except Exception as e:
        print(f"Error performing analysis: {e}")
        return {}

    return {}

if __name__ == "__main__":
    # Example usage
    sample_data = {
        'noaa_df': pd.DataFrame({
            'temperature': [20, 21, 19, 22, 23, 24],
            'humidity': [50, 55, 60, 65, 70, 75]
        })
    }
    perform_analysis(sample_data)
