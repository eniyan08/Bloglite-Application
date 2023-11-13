from flask_restful import Resource, reqparse, abort, Api, fields, marshal_with, marshal
from werkzeug.exceptions import InternalServerError, NotFound, HTTPException
from models import User as user_model, db
from models import Post as post_model, db
from models import Follower as follower_model, db
from models import Following as following_model, db
from models import Post_likes as like_model
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import sqlite3
import csv
from flask_security import auth_required
from security import user_datastore, sec 
from flask_security import hash_password
from tasks import task11, task22
# import app

# from app import cache

from time import perf_counter_ns
# from flask import current_app as app 
# from flask_caching import Cache

# config = {
#     "CACHE_TYPE" : "RedisCache",
#     "CACHE_REDIS_HOST" : "localhost",
#     "CACHE_REDIS_PORT" : 6379
# }  
# app.config.from_mapping(config)  
# app.app_context.push()
# cache = Cache(app)

# cache.init_app(app) 
# app.app_context.push()

api_v1 = Api(prefix='/api/')

task_req_data = reqparse.RequestParser()
task_req_data.add_argument('username', required=True, help="title required")
task_req_data.add_argument('email')
task_req_data.add_argument('password')

followers_req_data = reqparse.RequestParser()
followers_req_data.add_argument('friend_who_follows_user')
followers_req_data.add_argument('user_who_is_followedby')
followers_req_data.add_argument('avatar')   #this one should be removed

following_req_data = reqparse.RequestParser()
following_req_data.add_argument('user')
following_req_data.add_argument('current_user')
following_req_data.add_argument('avatar')

details_req_data = reqparse.RequestParser()
details_req_data.add_argument('avatar')
details_req_data.add_argument('username')
details_req_data.add_argument('name')
details_req_data.add_argument('bio')

post_data = reqparse.RequestParser()
post_data.add_argument('username')
post_data.add_argument('posts')
post_data.add_argument('caption')
post_data.add_argument('timestamp')
post_data.add_argument('avatar')

edit_post_data = reqparse.RequestParser()
edit_post_data.add_argument('posts')
edit_post_data.add_argument('caption')
edit_post_data.add_argument('timestamp')

likes_req_data = reqparse.RequestParser()
likes_req_data.add_argument('ID')
likes_req_data.add_argument('user')


post_like_data = reqparse.RequestParser()
post_like_data.add_argument('likes')


User_resource_field={
    'id':fields.Integer,
    'username':fields.String,
    'email':fields.String,
    'password':fields.String,
    'name':fields.String,
    'avatar':fields.String,
    'bio':fields.String,
    # 'following':fields.String,
    # 'followers':fields.String, 
    # 'following_no':fields.Integer,
    # 'followers_no':fields.Integer,
    'no_of_posts':fields.Integer,
    'active':fields.Boolean,
    'fs_uniquifier':fields.String
}

Followers_resource_field={
    'user_name':fields.String,
    'friend_who_follows_user':fields.String,
    'avatar':fields.String
    # 'followers_no':fields.Integer,
}

Following_resource_field={
    'user_name':fields.String,
    'friend':fields.String,
    'avatar':fields.String
    # 'followers_no':fields.Integer,
}

posts_resource_field={
    'username':fields.String,
    'posts':fields.String,
    'ID':fields.Integer,
    'likes':fields.Integer,
    'caption':fields.String,
    'timestamp':fields.String,
    'avatar':fields.String
}

likes_resource_field={
    'ID':fields.Integer,
    'user':fields.String
}


class Task(Resource):
 
    @marshal_with(User_resource_field)
    @auth_required('token')
    def get(self, email=None):
        if email:
            data = user_model.query.filter_by(email = email).first()
            if data:
                return marshal(data, User_resource_field)
            else:
                return "data not found"
    
    def post(self, username = None):
        if not username:
            data = task_req_data.parse_args()
            if not user_datastore.find_user(username = data.username):
                user_datastore.create_user(username = data.username,
                                           email = data.email, 
                                           password = hash_password(data.password))
                db.session.commit()
    
    @auth_required('token')
    def put(self, email=None):
        try:
            if email:
                new_data=details_req_data.parse_args()
                old_data = user_model.query.filter_by(email = email).first()
                try:
                    if 'username' in new_data.keys():
                        old_data.username = new_data.get('username')
                    if 'name' in new_data.keys():
                        old_data.name = new_data.get('name')
                    if 'avatar' in new_data.keys():
                        old_data.avatar = new_data.get('avatar')
                    if 'bio' in new_data.keys():
                        old_data.bio = new_data.get('bio')
                    try:
                        db.session.commit()
                        return "data updated"
                    except SQLAlchemyError:
                        raise InternalServerError('Data could not be added')
                except HTTPException as error:
                    raise error
                except BaseException:
                    raise InternalServerError('Something went wrong')
   
        except:
            return("username need")

# ------------------------------------------------------------------------------------------------------------------


class Followers(Resource):
    @marshal_with(Followers_resource_field)
    def get(self, user_name=None):
        if user_name:
            data = follower_model.query.filter_by(user_name = user_name).all()
            try:
                return data
            except:
                raise InternalServerError("coud not fetch the data")


    def post(self, user_name=None):
        try:
            data = followers_req_data.parse_args()
            if user_name:
                task = follower_model(
                    friend_who_follows_user = data.friend_who_follows_user,
                    user_name = data.user_who_is_followedby,
                    avatar = data.avatar)
                
                try:
                    db.session.add(task)
                    db.session.commit()
                    return "data added"
                except SQLAlchemyError:
                    raise InternalServerError('Data could not be added')
            else:
                abort(404, message='username not required')
            
        except HTTPException as error:
            raise error
        except BaseException:
            raise InternalServerError('Something went wrong')

    
    def delete(self, user_name=None, friend_who_follows_user=None):
        if user_name:
            data = follower_model.query.filter_by(user_name = user_name,
                                                  friend_who_follows_user = friend_who_follows_user).first()
            try:
                db.session.delete(data)
                db.session.commit()
                return "friend unfollowed you"
            except:
                raise InternalServerError("trouble in friend unfollowing you")

# ---------------------------------------------------------------------------------------------------------------


class Following(Resource):
    @marshal_with(Following_resource_field)
    def get(self, current_user=None):
        if current_user:
            data = following_model.query.filter_by(user_name = current_user).all()
            try:
                # db.session.delete(data)
                # db.session.commit()
                return data
            except:
                raise InternalServerError("coud not fetch the data")


    def post(self, current_user=None):
        if current_user:
            # if user:
                try: 
                    data = following_req_data.parse_args()                        
                    task1 = following_model(user_name = data.current_user,
                                   friend = data.user,
                                   avatar = data.avatar)
                    try:
                        db.session.add(task1)
                        db.session.commit()
                        
                        return "data added"
                    except SQLAlchemyError:
                        raise InternalServerError('Data could not be added')
                except BaseException:
                    raise InternalServerError('Something went wrong')
                
    
    def delete(self, current_user=None, user=None):

        if current_user:
            data = following_model.query.filter_by(user_name = current_user,
                                                    friend = user).first()
            try:
                # return data
                db.session.delete(data)
                db.session.commit()
                return "friend unfollowed"
            except:
                raise InternalServerError("coud not remove the data")
            
            
# --------------------------------------------------------------------------------------------------


class Details(Resource):

    # @marshal_with(Details_resource_field)
    @marshal_with(User_resource_field)
    @auth_required('token')
    def get(self, username=None):
        try:
            if username:
                try:
                    data = user_model.query.filter_by(username = username).first()
                    return data
                except:
                        raise InternalServerError("coud not fetch the data")
        except SQLAlchemyError:
            raise InternalServerError("Could not get the data")

    

# -----------------------------------------------------------------------------------------------------

class Post(Resource):

    @marshal_with(posts_resource_field)
    # @cache.cached(timeout=50)
    def get(self, user_name=None):
        if not user_name:
            data = post_model.query.all()
            try:
                
                return data
            except:
                raise InternalServerError("coud not fetch the data")

    def post(self, user_name=None):
        if user_name:
            data = post_data.parse_args()
            task = post_model(username = data.username,
                            posts = data.posts,
                            caption = data.caption,
                            timestamp = data.timestamp,
                            avatar = data.avatar)
            try:
                db.session.add(task)
                db.session.commit()
                job_id = task11(user_name)
                return str(job_id)


            except SQLAlchemyError:
                raise InternalServerError('Data could not be added')
        else:
            return "username needed"
        
    def delete(self, user_name=None):
        if user_name:
            data = post_model.query.filter_by(username = user_name).all()
            try:
                db.session.delete(data[5])
                db.session.commit()
                return "post deleted"
            except:
                raise InternalServerError("coud not remove the data")

#--------------------------------------------------------------------------------------------------------------------------------------


class PostLike(Resource):

    @marshal_with(likes_resource_field)
    def get(self, ID=None, user=None):
        if ID:
            data = like_model.query.filter_by(ID = ID, user = user).first()
            try:
                return data
            except:
                raise InternalServerError("coud not fetch the data")
        
    def post(self, ID=None):
        if ID:
            data = likes_req_data.parse_args()
            task = like_model(ID = data.ID,
                              user = data.user)
            try:
                db.session.add(task)
                db.session.commit()
                return "like data successfully added"
            except:
                return "something terrible happened"
            
    def delete(self, ID=None, user=None):
        if ID:
            data = like_model.query.filter_by(ID = ID, user = user).first()
            try:
                db.session.delete(data)
                db.session.commit()
                return "like data deleted"
            except:
                raise InternalServerError("coud not remove the data")
            
#-------------------------------------------------------------------------------------------------------------------------------

class UserPosts(Resource):
    
    @marshal_with(posts_resource_field)
    def get(self, username=None):
        if username:
            data = post_model.query.filter_by(username = username).all()
            try:
                return data
            except:
                raise InternalServerError("coud not fetch the data")
            
    

#---------------------------------------------------------------------------------------------

class Boredom(Resource):

    @marshal_with(posts_resource_field)
    def get(self, ID=None):
        if ID:
            data = post_model.query.filter_by(ID = ID).first()
            try:
                return data
            except:
                raise InternalServerError("coud not fetch the data")

    def delete(self, ID=None):
        if ID:
            data = post_model.query.filter_by(ID = ID).first()
            try:
                db.session.delete(data)
                db.session.commit()
                return "post deleted"
            except:
                raise InternalServerError("coud not delete the post")
#--------------------------------------------------------------------------------------------------------------

class post_like(Resource):
    def put(self, ID = None):
        if ID:
            data = post_like_data.parse_args()
            old_data = post_model.query.filter_by(ID = ID).first()
            try:
                if 'likes' in data.keys():
                    old_data.likes = data.get('likes')

                try:
                    db.session.commit()
                    return "data updated"
                except SQLAlchemyError:
                    raise InternalServerError('Data could not be added')
            except HTTPException as error:
                raise error
            except BaseException:
                raise InternalServerError('Something went wrong')
            
#---------------------------------------------------------------------------------------------------------         

class edit_post(Resource):
    def put(self, ID=None):
        if ID:
            data = edit_post_data.parse_args()
            old_data = post_model.query.filter_by(ID = ID).first()
            try:
                if 'posts' in data.keys():
                    old_data.posts = data.get('posts')
                if 'caption' in data.keys():
                    old_data.caption = data.get('caption')
                if 'timestamp' in data.keys():
                    old_data.timestamp = data.get('timestamp')
                try:
                    db.session.commit()
                    return "post data updated"
                except SQLAlchemyError:
                    raise InternalServerError('post Data could not be added')
            except HTTPException as error:
                raise error
            except BaseException:
                raise InternalServerError('Something went wrong')
            
#------------------------------------------------------------------------------------------------

class export_post(Resource):

    @marshal_with(posts_resource_field)
    def get(self, ID=None):
        if ID:
            data = post_model.query.filter_by(ID = ID).first()
            try:
                main_list=[]
                list=[]
                field_names = ['username', 'posts', 'ID', 'likes', 'caption', 'timestamp', 'avatar']
                # with open('Names.csv', 'w') as csvfile:
                #     writer = csv.DictWriter(csvfile, fieldnames = field_names)
                #     writer.writeheader()
                #     writer.writerows(data)
                
                list.append(data.username)
                list.append(data.posts)
                list.append(str(data.ID))
                list.append(str(data.likes))
                list.append(data.caption)
                list.append(data.timestamp)
                list.append(data.avatar)
                # print(str(data.ID))
                # print(list)
                
                main_list.append(list)
                # print(main_list)
                with open('Names1.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(field_names)
                    writer.writerows(main_list)
                job2 = task22.delay()
                data = str(job2.get())
                return data
            except:
                raise InternalServerError("coud not fetch the data")
        

#---------------------------------------------------------------------------------------------------------------------------------------------

api_v1.add_resource(Task, 'tasks', 'tasks/<string:email>')

api_v1.add_resource(Followers, 'followers', 'followers/<string:user_name>', 'followers/<string:user_name>/<string:friend_who_follows_user>')

api_v1.add_resource(Following, 'following', 'following/<string:current_user>', 'following/<string:current_user>/<string:user>')

api_v1.add_resource(Details, 'details', 'details/<string:username>')

api_v1.add_resource(Post, 'posts', 'posts/<string:user_name>')

api_v1.add_resource(PostLike, 'postlike', 'postlike/<int:ID>', 'postlike/<int:ID>/<string:user>')

api_v1.add_resource(UserPosts, 'userposts', 'userposts/<string:username>')

api_v1.add_resource(post_like, 'post', 'post/<int:ID>')

api_v1.add_resource(Boredom, 'boredom', 'boredom/<int:ID>')

api_v1.add_resource(edit_post, 'edit_post', 'edit_post/<int:ID>')

api_v1.add_resource(export_post, 'export_post', 'export_post/<int:ID>', 'export_post/<int:ID>/<string:user>')
# from app import cache