import requests

def fetch_weather_data():
    url = "http://api.weatherapi.com/v1/current.json?key=af53e4aa3bb84f8391b61235241712&q=London&aqi=no"
    
    try:
        # Send a GET request to the weather API
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response as JSON
            weather_data = response.json()
            return weather_data
        else:
            print(f"Error: Unable to fetch data, status code {response.status_code}")
    
    except Exception as e:
        print(f"Error fetching weather data: {e}")

# Call the function and print the result
weather_data = fetch_weather_data()
if weather_data:
    print(weather_data)
