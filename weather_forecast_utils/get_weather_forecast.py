import requests
from datetime import datetime, timedelta
from weather_forecast_utils import get_city_coords
from constants import OPEN_WEATHER_APY_TOKEN

from weather_forecast_utils.custom_typings import ForecastType

OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def weather_forecast(city_name: str, for_current_date: datetime) -> ForecastType:
    coords = get_city_coords(city_name)

    query_params = {
        'lat': coords['latitude'],
        'lon': coords['longtide'],
        'appid': OPEN_WEATHER_APY_TOKEN,
        'lang': 'rus,',
        'units': 'metric'

    }
    r = requests.get(url=OPEN_WEATHER_URL, params=query_params)
    next_5_days_forecasts = r.json()['list']

    def is_current_day_forecast(forecast: ForecastType) -> bool:
        forecast_date_unix = int(forecast['dt'])

        return for_current_date.timestamp() <= forecast_date_unix < (for_current_date + timedelta(days=1)).timestamp()

    current_date_forecast = list(filter(lambda f: is_current_day_forecast(f), next_5_days_forecasts))

    return current_date_forecast[int(len(current_date_forecast) / 2)]