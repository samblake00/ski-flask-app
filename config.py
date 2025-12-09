# encoding: utf-8

class BaseConfig(object):
    ENABLED_MODULES = {
        'api',
        'ski',
    }

    SWAGGER_UI_JSONEDITOR = True


class DevelopmentConfig(BaseConfig):
    """config for DevelopmentConfig."""
    DEBUG = True
    DEVELOPMENT = True

    # Database (prototype uses sqlite file)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Scheduler
    SCHEDULER_ENABLED = False
    SCHEDULER_POLL_INTERVAL_MINUTES = 5

    # Providers
    ENABLE_REAL_PROVIDERS = False