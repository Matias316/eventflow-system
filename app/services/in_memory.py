from redis import Redis

class FlaskRedis:

    def __init__(self):
        self.client = None

    def init_app(self, app):
        self.client = Redis.from_url(app.config["REDIS_URL"])

    def get_client(self):
        return self.client

redis_client = FlaskRedis()