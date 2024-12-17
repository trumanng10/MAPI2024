import React, { useState } from "react";

function App() {
  const [city, setCity] = useState(""); // State to hold the city input
  const [weatherData, setWeatherData] = useState(null);
  const [error, setError] = useState("");

  const fetchWeatherData = async () => {
    const url = `https://api.weatherapi.com/v1/current.json?key=af53e4aa3bb84f8391b61235241712&q=${city}&aqi=no`;

    try {
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setWeatherData(data);
        setError(""); // Clear any previous errors
      } else {
        setError(`Failed to fetch weather data for ${city}.`);
      }
    } catch (err) {
      console.error("Error fetching weather data:", err);
      setError("Failed to fetch weather data. Please try again.");
    }
  };

  return (
    <div
      style={{
        fontFamily: "Arial, sans-serif",
        textAlign: "center",
        backgroundColor: "#f0f8ff",
        color: "#333",
        padding: "20px",
      }}
    >
      <h1>Weather App</h1>
      <div>
        <input
          type="text"
          placeholder="Enter city name"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          style={{
            padding: "10px",
            marginRight: "10px",
            border: "1px solid #ccc",
            borderRadius: "5px",
            width: "200px",
          }}
        />
        <button
          onClick={fetchWeatherData}
          style={{
            padding: "10px 20px",
            backgroundColor: "#007BFF",
            color: "white",
            border: "none",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Get Weather
        </button>
      </div>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {weatherData && (
        <div
          style={{
            marginTop: "20px",
            border: "1px solid #ccc",
            borderRadius: "10px",
            padding: "20px",
            display: "inline-block",
            backgroundColor: "white",
            textAlign: "left",
          }}
        >
          <h2>
            {weatherData.location.name}, {weatherData.location.country}
          </h2>
          <p>
            <strong>Temperature:</strong> {weatherData.current.temp_c}°C /{" "}
            {weatherData.current.temp_f}°F
          </p>
          <p>
            <strong>Condition:</strong> {weatherData.current.condition.text}
          </p>
          <img
            src={weatherData.current.condition.icon}
            alt={weatherData.current.condition.text}
          />
          <p>
            <strong>Wind:</strong> {weatherData.current.wind_kph} kph (
            {weatherData.current.wind_dir})
          </p>
          <p>
            <strong>Humidity:</strong> {weatherData.current.humidity}%
          </p>
          <p>
            <strong>Last Updated:</strong> {weatherData.current.last_updated}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
