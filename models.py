import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), nullable=False)
    posts = relationship(
        'Post',
        order_by='Post.created_dt',
        back_populates='user',
    )


class Image(BaseModel):
    __tablename__ = 'Image'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(100))


class Post(BaseModel):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250), nullable=False)
    body = Column(Text,  nullable=False)
    created_dt = Column(DateTime, default=datetime.datetime.now)
    images = relationship('Image', secondary='image_post')
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    user = relationship(
        'User',
        foreign_keys=[user_id],
        back_populates='posts',
    )


class ImagePost(BaseModel):
    __tablename__ = 'image_post'
    image_id = Column(Integer, ForeignKey('Image.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'), primary_key=True)