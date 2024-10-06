# run_api.py
from flask import Flask, jsonify, request
from data_storage.models.weather_model import session, WeatherData

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Advanced Weather Application API"

@app.route('/api/v1/weather', methods=['GET'])
def get_weather_data():
    """Endpoint to get stored weather data."""
    data = session.query(WeatherData).all()
    weather_list = [
        {
            "id": entry.id,
            "temperature": entry.temperature,
            "humidity": entry.humidity,
            "wind_speed": entry.wind_speed,
            "datetime": entry.datetime,
            "source": entry.source
        } for entry in data
    ]
    return jsonify(weather_list)

@app.route('/api/v1/weather', methods=['POST'])
def add_weather_data():
    """Endpoint to add new weather data."""
    try:
        data = request.json
        new_weather_data = WeatherData(**data)
        session.add(new_weather_data)
        session.commit()
        return jsonify({"message": "Weather data added successfully"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400

def start_api():
    """Run the Flask API server."""
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    start_api()
