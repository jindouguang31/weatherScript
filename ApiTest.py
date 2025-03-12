import requests
import pytest

def test_api_response():
    url = "https://api.weather.gov/gridpoints/HKO/31,80/forecast"
    response = requests.get(url)
    
    # Check if the request was successful
    assert response.status_code == 200
    
    # Extract the relative humidity for the day after tomorrow
    forecast_data = response.json()
    day_after_tomorrow_forecast = forecast_data['properties']['periods'][2]
    relative_humidity = day_after_tomorrow_forecast['relativeHumidity']['value']
    
    # Assert that the relative humidity is within expected range
    assert 0 <= relative_humidity <= 100
    print(f"Relative Humidity for the day after tomorrow: {relative_humidity}%")

if __name__ == "__main__":
    test_api_response()