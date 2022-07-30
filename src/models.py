import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("follow_id", ForeignKey("follow.id")),
)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_email = Column(String(250), nullable=False)
    user_password = Column(String(100), nullable=False)
    login_status = Column(String(250), nullable=False)
    user_name = Column(String(100), nullable=False)
    user_full_name = Column(String(250), nullable=False)
    block_id = Column(Integer, ForeignKey('block.id'))
    likes_id = Column(Integer, ForeignKey('likes.id'))
    follow = relationship("Follow", secondary=association_table)


class Follow(Base):
    __tablename__ = "follow"
    id = Column(Integer, primary_key=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))
    hashtag_id = Column(Integer, ForeignKey('hashtag.id'))
    likes_id = Column(Integer, ForeignKey('likes.id'))
    
    
class Block(Base):
    __tablename__ = 'block'
    id = Column(Integer, primary_key=True)
   

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(1000), nullable=False)
    likes_id = Column(Integer, ForeignKey('likes.id'))


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    
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