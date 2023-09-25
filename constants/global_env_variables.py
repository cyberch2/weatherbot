import os

BOT_TOKEN = os.environ.get('6581380313:AAGTRVLMKxSZME8qyvpXp-RJsDw2OLqZDls')
YANDEX_GEOCODER_API_TOKEN = os.environ.get('52175b67-8f6e-4044-90ad-e7c21b494279')
OPEN_WEATHER_APY_TOKEN = os.environ.get('75cece817babd6a357e973fa2c338625')


def check_all_tockens_set():
    return BOT_TOKEN is not None and YANDEX_GEOCODER_API_TOKEN is not None and OPEN_WEATHER_APY_TOKEN is not None

