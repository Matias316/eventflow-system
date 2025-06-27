class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = "amqp://guest@localhost//"
    REDIS_URL = "redis://localhost:6379/0"

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://devuser:devpass@localhost/devdb"

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

# TODO: Review production parameters
# class ProductionConfig(BaseConfig):
#    SQLALCHEMY_DATABASE_URI = "postgresql://produser:prodpass@db/proddb"
