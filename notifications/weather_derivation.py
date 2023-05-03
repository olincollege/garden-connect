"""Doc"""
import requests
from api_key import _api_key


def weather_data(city):
    """
    Docstring
    """
    url = f"http://api.weatherstack.com/current?access_key={_api_key}&query={city}"
    response = requests.get(url)
    data = response.json()
    return {
        "temperature": data["current"]["temperature"],
        "precipitation": data["current"]["precip"],
        "humidity": data["current"]["humidity"],
    }
