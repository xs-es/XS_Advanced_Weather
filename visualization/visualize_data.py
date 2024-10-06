# visualize_data.py
import matplotlib.pyplot as plt
import pandas as pd

def create_visualizations(analysis_results):
    """Create visualizations from analyzed data."""
    try:
        df = analysis_results.get('data')
        if df is not None:
            # Example: Create a line plot of temperature over time
            plt.plot(df['period'], df['temperature'], marker='o')
            plt.title('Temperature Trend Over Time')
            plt.xlabel('Period')
            plt.ylabel('Temperature (°C)')
            plt.grid(True)
            plt.show()

            print("Visualization created successfully.")
    except Exception as e:
        print(f"Error creating visualization: {e}")

if __name__ == "__main__":
    # Example usage
    sample_data = {
        'data': pd.DataFrame({
            'temperature': [20, 21, 19, 22, 23, 24],
            'period': [1, 2, 3, 4, 5, 6]
        })
    }
    create_visualizations(sample_data)
