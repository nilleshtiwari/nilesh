from flaskApp import create_app
from logging.config import dictConfig
from config import LoggingConfig

# logging Configurations
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': LoggingConfig.format,
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    },
        'fileHandlerLog': {
            'class': 'logging.FileHandler',
            'filename': LoggingConfig.filename,
            'formatter': 'default'
        }},
    'root': {
        'level': LoggingConfig.level,
        'handlers': ['wsgi', 'fileHandlerLog']
    }
})



app = create_app()

if __name__ == "__main__":
    app.logger.info("App started...")
    app.run(host="0.0.0.0")
