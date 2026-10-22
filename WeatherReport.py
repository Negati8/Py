import requests
from dataclasses import dataclass
@dataclass
class WeatherReport:
    city: str
    country: str
    temp: float
    feels_like: float
    wind: float
    min_tomorrow: float
    max_tomorrow: float

    def __str__(self):
        return (
            f" {self.city}, {self.country}\n"
            f" Сейчас: {self.temp}°C (ощущается как {self.feels_like}°C)\n"
            f" Ветер: {self.wind} км/ч\n"
            f" Завтра: от {self.min_tomorrow}°C до {self.max_tomorrow}°C"
        )

class WeatherService:
    def __init__(self):
        self.timeout = 10  

    def get_weather(self, city: str) -> WeatherReport:
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {"name": city, "count": 1, "language": "ru"}
        
        geo_response = requests.get(geo_url, params=geo_params, timeout=self.timeout)
        geo_response.raise_for_status() 
        
        geo_data = geo_response.json()
        if not geo_data.get("results"):
            raise ValueError(f"Город '{city}' не найден. Проверьте название.")
            
        location = geo_data["results"][0] 
        
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": "temperature_2m,apparent_temperature,wind_speed_10m",
            "daily": "temperature_2m_min,temperature_2m_max",
            "timezone": "auto",
            "forecast_days": 2  
        }
        
        weather_response = requests.get(weather_url, params=weather_params, timeout=self.timeout)
        weather_response.raise_for_status()
        w_data = weather_response.json()
        
        return WeatherReport(
            city=location["name"],
            country=location.get("country", "Неизвестная страна"),
            temp=w_data["current"]["temperature_2m"],
            feels_like=w_data["current"]["apparent_temperature"],
            wind=w_data["current"]["wind_speed_10m"],
            min_tomorrow=w_data["daily"]["temperature_2m_min"][1],
            max_tomorrow=w_data["daily"]["temperature_2m_max"][1]
        )

if __name__ == "__main__":
    service = WeatherService()
    user_city = input("Введите название города: ").strip()
    try:
        report = service.get_weather(user_city)
        print("\n" + str(report)) 
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Сетевая ошибка (нет интернета или упал сервер): {e}")
    except Exception as e:
        print(f"Что-то пошло не так: {e}")