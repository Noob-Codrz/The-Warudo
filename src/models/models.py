from sqlalchemy import Column, Integer, String, ForeignKey, Float, Time, Boolean, DateTime, Text
from uuid import uuid4
import datetime
from sqlalchemy.orm import relationship


class User_forAuth:
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100)) ## hash this or store in vault
    is_disabled = Column(Boolean, default=False)
    

class User:
    __tablename__ = 'user_details'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    phone = Column(String(10), unique=True)
    profile_pic = Column(String(100)) ## store in s3
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    birth_date = Column(DateTime)
    gender = Column(String(10))
    bio = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    twitter_id = Column(String(100))
    instagaram_id = Column(String(100), default="NA")
    followers = Column(Integer, ForeignKey("user.id"))
    following = Column(Integer, ForeignKey("user.id"))
    admin_status = Column(Boolean, default=False)
    admin_status_val = Column(String(100), default="NA")
    
    contents = relationship("Content", back_populates="user")
    bookmarks = relationship("Bookmark", back_populates="bookmark_user")


class Content:
    __tablename__ = 'content'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    category = Column(Integer, ForeignKey("category.id"))
    sub_category = Column(Integer, ForeignKey("sub_category.id"))
    user = Column(Integer, ForeignKey("user.id")) 
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    likes = Column(Integer, default=0)
    # comments = Column(Text) ## make so as to store Foriegn key for multiple comments
    citation = Column(Text)
    is_public = Column(Boolean, default=False)
    head_comments = Column(Integer, ForeignKey("comments.id"))
    user = relationship("User", back_populates="contents")
    
    comments = relationship("Comments", back_populates="content")
    
class Comments:
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, index=True)
    comment_content = Column(Text)
    comment_likes = Column(Integer, default=0)
    comment_user = Column(Integer, ForeignKey("user.id"))
    comment_created_at = Column(DateTime, default=datetime.datetime.utcnow)
    comment_updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    flag_is_updated = Column(Boolean, default=False)
    flag_show = Column(Boolean, default=True)
    flag_comment_of_comment = Column(Boolean, default=False)
    
class Content_comment:
    __tablename__ = "content_comment"
    
    id = Column(Integer, primary_key = True, index = True)
    content_id = Column(Integer, ForeignKey("content.id"))
    comment_id = Column(Integer, ForeignKey("comments.id"))
    
    content = relationship("Content", back_populates="comments")
    
class Comment_comment:
    __tablename__ = "comments_comment"
    id = Column(Integer, primary_key = True, index = True)
    head_comment_id = Column(Integer, ForeignKey("comments.id"))
    reply_comment_id = Column(Integer, ForeignKey("comments.id"))

    
class Category:
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True, index=True)
    categioy_name = Column(String(100))
    category_description = Column(Text)
    category_pic = Column(String(100)) ## store in s3
    
class Sub_Category:
    __tablename__ = 'sub_category'
    
    id = Column(Integer, primary_key=True, index=True)
    sub_categioy_name = Column(String(100))
    sub_category_description = Column(Text)
    sub_category_pic = Column(String(100)) ## store in s3
    category_id = Column(Integer, ForeignKey("category.id"))
    
    
    
class Collection:
    __tablename__ = 'collection'
    
    id = Column(Integer, primary_key=True, index=True)
    collection_name = Column(String(100))
    collection_description = Column(Text)
    colection_user = Column(Integer, ForeignKey("user.id"))
    collection_posts = Column(Integer, ForeignKey("content.id"))
    
class Bookmark:
    __tablename__ = 'bookmark'
    
    id = Column(Integer, primary_key=True, index=True)
    bookmark_user = Column(Integer, ForeignKey("user.id"))
    bookmark_content = Column(Integer, ForeignKey("content.id"))
    
    user = relationship("User", back_populates="bookmarks")