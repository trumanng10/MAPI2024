from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Define the base URL for the weather API
API_URL = "http://api.weatherapi.com/v1/current.json?key=af53e4aa3bb84f8391b61235241712&q=London&aqi=no"

# Route 1: Get weather data for London
@app.route('/weather', methods=['GET'])
def get_weather():
    try:
        # Send a request to the WeatherAPI to get current weather data
        response = requests.get(API_URL)
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Convert the response to JSON
            return jsonify(data), 200
        else:
            return jsonify({"error": "Unable to fetch weather data"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route 2: Health Check - to verify the app is running
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "Service is up and running!"}), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
