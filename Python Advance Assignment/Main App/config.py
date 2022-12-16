import logging
from pathlib import Path

base_dir = Path(__file__).parent


class Config(object):
    """Common configurations"""
    pass


class DevelopmentConfig(object):
    """Development configurations"""
    DEBUG = True
    # To log errors


class ProductionConfig(object):
    """Production configurations"""
    DEBUG = False


class LoggingConfig(object):
    filename = Path(base_dir, 'app.log')
    filemode = 'w'
    format = "[%(asctime)s] %(levelname)s | %(module)s >>> %(message)s"
    datefmt = "%B %d, %Y %H:%M:%S %Z"
    level = logging.DEBUG


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'logging': LoggingConfig
}
