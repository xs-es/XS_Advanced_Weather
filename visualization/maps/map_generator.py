# map_generator.py
import folium

def generate_weather_map(lat, lon, weather_description):
    """Generate a weather map using Folium."""
    try:
        weather_map = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker(
            [lat, lon],
            popup=f"Weather: {weather_description}",
            icon=folium.Icon(icon="cloud")
        ).add_to(weather_map)
        
        # Save map to HTML file
        weather_map.save("weather_map.html")
        print("Weather map generated successfully.")
    except Exception as e:
        print(f"Error generating map: {e}")

if __name__ == "__main__":
    # Example usage
    generate_weather_map(39.8283, -98.5795, "Sunny with scattered clouds")
