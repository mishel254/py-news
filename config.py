import os

class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=all&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SOURCE_API_URL = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'

class prodConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':prodConfig
}
