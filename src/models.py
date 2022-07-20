import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Instagram(Base):
    __tablename__ = 'insta_database'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    users_email = Column(String(250), nullable=False)
    users_password = Column(String(100), nullable=False)
    login_status = Column(String(250), nullable=False)
    users_name = Column(String(100), nullable=False)
    users_full_name = Column(String(250), nullable=False)
    

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    following_id = Column(Integer, ForeignKey('following.id'))
    followers_id = Column(Integer, ForeignKey('followers.id'))
    block_id = Column(Integer, ForeignKey('block.id'))
    feed_id = Column(Integer, ForeignKey('feed.id'))
    likes_id = Column(Integer, ForeignKey('likes.id'))

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))


class Feed(Base):
    __tablename__ = 'feed'
    id = Column(Integer, primary_key=True)
    
    posts_id = Column(Integer, ForeignKey('posts.id'))
    
class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    
class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    
   
class Block(Base):
    __tablename__ = 'block'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_content = Column(String(1000), nullable=False)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    hashtag_id = Column(Integer, ForeignKey('hashtag.id'))
    likes_id = Column(Integer, ForeignKey('likes.id'))
    

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    likes_id = Column(Integer, ForeignKey('likes.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    
    

class PostLocation(Base):
    __tablename__ = 'post_location'
    id = Column(Integer, primary_key=True)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    

class Hashtag(Base):
    __tablename__ = 'hashtag'
    id = Column(Integer, primary_key=True)
    hashtag = Column(String(1000), nullable=False)
   



    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e