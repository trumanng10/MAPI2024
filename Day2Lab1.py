import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data
def fetch_weather_data():
    url = "http://api.weatherapi.com/v1/current.json?key=af53e4aa3bb84f8391b61235241712&q=London&aqi=no"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            messagebox.showerror("Error", f"Unable to fetch data. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")

# Function to display weather data in the GUI
def display_weather():
    weather_data = fetch_weather_data()
    if weather_data:
        location = f"{weather_data['location']['name']}, {weather_data['location']['country']}"
        temperature = f"{weather_data['current']['temp_c']}°C / {weather_data['current']['temp_f']}°F"
        condition = weather_data['current']['condition']['text']
        wind = f"{weather_data['current']['wind_kph']} kph ({weather_data['current']['wind_dir']})"
        humidity = f"{weather_data['current']['humidity']}%"
        last_updated = weather_data['current']['last_updated']

        # Update labels with weather data
        location_label.config(text=f"Location: {location}")
        temperature_label.config(text=f"Temperature: {temperature}")
        condition_label.config(text=f"Condition: {condition}")
        wind_label.config(text=f"Wind: {wind}")
        humidity_label.config(text=f"Humidity: {humidity}")
        last_updated_label.config(text=f"Last Updated: {last_updated}")

# Create the main GUI window
root = tk.Tk()
root.title("Weather Viewer")
root.geometry("400x400")
root.configure(bg="#f0f8ff")

# Header
header = tk.Label(root, text="Weather Information", font=("Arial", 18, "bold"), bg="#f0f8ff")
header.pack(pady=10)

# Weather Data Labels
location_label = tk.Label(root, text="Location: ", font=("Arial", 12), bg="#f0f8ff")
location_label.pack(anchor="w", padx=20)

temperature_label = tk.Label(root, text="Temperature: ", font=("Arial", 12), bg="#f0f8ff")
temperature_label.pack(anchor="w", padx=20)

condition_label = tk.Label(root, text="Condition: ", font=("Arial", 12), bg="#f0f8ff")
condition_label.pack(anchor="w", padx=20)

wind_label = tk.Label(root, text="Wind: ", font=("Arial", 12), bg="#f0f8ff")
wind_label.pack(anchor="w", padx=20)

humidity_label = tk.Label(root, text="Humidity: ", font=("Arial", 12), bg="#f0f8ff")
humidity_label.pack(anchor="w", padx=20)

last_updated_label = tk.Label(root, text="Last Updated: ", font=("Arial", 12), bg="#f0f8ff")
last_updated_label.pack(anchor="w", padx=20)

# Button to Fetch Weather Data
fetch_button = tk.Button(root, text="Get Weather", command=display_weather, bg="#007BFF", fg="white", font=("Arial", 12), relief="flat")
fetch_button.pack(pady=20)

# Run the application
root.mainloop()
