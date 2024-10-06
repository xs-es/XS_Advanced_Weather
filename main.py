# main.py
from data_acquisition.acquire_data import acquire_weather_data
from analytics.analyze_data import perform_analysis
from visualization.visualize_data import create_visualizations
from api.run_api import start_api
from notifications.send_notifications import send_weather_alerts

def main():
    print("Starting Weather App...")

    # Step 1: Acquire Data
    print("Acquiring Data...")
    data = acquire_weather_data()

    # Step 2: Perform Analysis
    print("Performing Data Analysis...")
    analysis_results = perform_analysis(data)

    # Step 3: Create Visualizations
    print("Creating Visualizations...")
    create_visualizations(analysis_results)

    # Step 4: Start API
    print("Starting API Service...")
    start_api()

    # Step 5: Send Notifications
    print("Sending Notifications...")
    send_weather_alerts(analysis_results)

if __name__ == "__main__":
    main()
