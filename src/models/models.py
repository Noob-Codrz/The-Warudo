from sqlalchemy import Column, Integer, String, ForeignKey, Float, Time, Boolean, DateTime, Text
import datetime



class User:
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100)) ## hash this or store in vault
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
    instagaram_id = Column(String(100)default="NA")
    followers = Column(Integer, ForeignKey("user.id"))
    following = Column(Integer, ForeignKey("user.id"))
    admin_status = Column(Boolean, default=False)
    admin_status_val = Column(String(100), default="NA")


class Content:
    __tablename__ = 'content'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    category = Column(Integer, ForeignKey("category.id"))
    sub_category = Column(Integer, ForeignKey("sub_category.id"))
    user = Column(Integer, ForeignKey("user.id")) 
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    likes = Column(Integer, default=0)
    comments = Column(Text)
    citation = Column(Text)
    is_public = Column(Boolean, default=True)
    
class Comments:
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("content.id"))
    comment_content = Column(Text)
    comment_likes = Column(Integer, default=0)
    comment_user = Column(Integer, ForeignKey("user.id"))
    comment_created_at = Column(DateTime, default=datetime.datetime.utcnow)
    comment_updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    flag_is_updated = Column(Boolean, default=False)
    flag_show = Column(Boolean, default=True)
    flag_comment_of_comment = Column(Boolean, default=False)
    
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
    
    