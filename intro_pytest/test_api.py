import random


class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city, country):
        temperature = random.randint(-20, 40)
        if country.lower() == "mx":
            description = "Sunny"
        elif country.lower() == "us":
            description = "Snowy"
        else:
            descriptions = ["Sunny", "Cloudy", "Rainy", "Snowy"]
            description = random.choice(descriptions)  # descripción aleatoria del clima
        return {
            "city": city,
            "country": country,
            "temperature": temperature,
            "description": description,
        }


def test_reply():
    api = WeatherAPI("TestAPI")
    result = api.get_weather("ontario", "ca")
    expected_keys = ["city", "country", "temperature", "description"]
    for field in expected_keys:
        assert field in result, f"API response should include {field}"


def test_mx_weather():
    api = WeatherAPI("TestAPI")
    result = api.get_weather("guadalajara", "mx")
    assert "description" in result, "Result response should include description"
    assert result["description"] == "Sunny", "MX should return Sunny"


def test_us_weather():
    api = WeatherAPI("TestAPI")
    result = api.get_weather("los angeles", "us")
    assert "description" in result, "Result response should include description"
    assert result["description"] == "Snowy", "US should return Snowy"