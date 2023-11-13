from celery import Celery
from flask import current_app as app   # to avoid circular dependency  ( watch week 10 livesession - 1:33)
# from flask_caching import Cache
from resource import api
# from app import app
celery = Celery("sample job")

class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

# config = {
#     "CACHE_TYPE" : "RedisCache",
#     "CACHE_REDIS_HOST" : "localhost",
#     "CACHE_REDIS_PORT" : 6379
# }      
# app.config.from_mapping(config)  

# cache = Cache(app)

# cache.init_app(app)

# app.app_context.push()

# api.init_app(app)