from config import DevelopmentConfig
from flask import Flask
from models import db

from flask_cors import CORS
from flask_sse import sse
from flask_caching import Cache
from flask_security import user_datastore, sec 

# from tasks import task11
# from tasks import make_celery

from time import perf_counter_ns
from werkzeug.exceptions import InternalServerError
from flask_restful import Resource, reqparse, abort, Api, fields, marshal_with, marshal
import jsonpickle
from sqlalchemy.exc import SQLAlchemyError

# post_data = reqparse.RequestParser()
# post_data.add_argument('username')
# post_data.add_argument('posts')
# post_data.add_argument('caption')
# post_data.add_argument('timestamp')
# post_data.add_argument('avatar')

posts_resource_field={
    'username':fields.String,
    'posts':fields.String,
    'ID':fields.Integer,
    'likes':fields.Integer,
    'caption':fields.String,
    'timestamp':fields.String,
    'avatar':fields.String
}

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.config.update(
      CELERY_BROKER_URL='redis://localhost:6379',
      CELERY_RESULT_BACKEND='redis://localhost:6379'
    )
    CORS(app) 
    # app.app_context.push()
    # cache = Cache(app)
    # cache.init_app(app) 
    
    db.init_app(app)
    sec.init_app(app, user_datastore) 
    app.register_blueprint(sse, url_prefix = "/stream")
    return app

app = create_app()
# app.app_context.push()
cache = Cache(app)
cache.init_app(app)
from resource import api_v1
# app.app_context.push()
api_v1.init_app(app)
# app.app_context.push()

@app.before_first_request
def create_db():
    db.create_all()



# from models import Post as post_model, db
# @app.route("/posts", methods=["GET"])
# # @cache.cached(timeout=50)
# @marshal_with(posts_resource_field)
# def get():
    
#     # start = perf_counter_ns()
#     data= post_model.query.all()
 
#     # stop = perf_counter_ns()
#     res_list = list(enumerate(data))
#     # time_taken = stop-start
#     try:
#         # print(time_taken)
#         # return data
#         return res_list
#     except:
#         raise InternalServerError("coud not fetch the data")
    

if __name__ == "__main__":
    app.run(debug=True, port='5002')