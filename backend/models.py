from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),)
        # db.Column('post_id', db.Integer(), db.ForeignKey('post.ID')))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String(225), unique=True)
    password = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String)
    avatar = db.Column(db.String)
    bio = db.Column(db.String)

    no_of_posts = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)

    # users = db.relationship("Post")
    roles = db.relationship('Role', secondary = roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(255))


class Post(db.Model):
    __tablename__ = 'post'
    username = db.Column(db.String, db.ForeignKey("user.username"))
    posts = db.Column(db.String)
    ID = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    likes = db.Column(db.Integer)
    caption = db.Column(db.String)
    timestamp = db.Column(db.String)  #  integer
    avatar = db.Column(db.String, db.ForeignKey("user.avatar"))
    # roles2 = db.relationship('User', secondary = roles_users, lazy="subquery")
    # followers_who_liked = 
 
class Post_likes(db.Model):
    __tablename__ = "post_likes"
    ID = db.Column(db.Integer, db.ForeignKey("post.ID"))
    user = db.Column(db.String)
    no3 = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Following(db.Model):
    __tablename__ = 'following'
    user_name = db.Column(db.String, db.ForeignKey("user.username"))
    no1 = db.Column(db.Integer, primary_key=True, autoincrement=True)
    friend = db.Column(db.String)
    avatar = db.Column(db.String, db.ForeignKey("user.avatar"))
    # following_no = db.Column(db.Integer)

class Follower(db.Model):
    __tablename__ = 'follower'
    user_name = db.Column(db.String, db.ForeignKey("user.username"))
    friend_who_follows_user = db.Column(db.String)
    no2 = db.Column(db.Integer, primary_key=True, autoincrement=True)
    avatar = db.Column(db.String, db.ForeignKey("user.avatar"))
    # followers_no = db.Column(db.Integer)