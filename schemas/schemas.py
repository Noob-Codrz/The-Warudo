from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
######################################################
################### Users ############################
######################################################


class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Optional[str] = None
    
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    
class UserPasswd(User):
    hashed_password: str
    
class UserDetails(User):
    phone: str
    profile_pic: Optional[str] = None
    birth_date: Optional[datetime] = None
    gender: Optional[str] = None
    bio: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    twitter_id: Optional[str] = None
    instagaram_id: Optional[str] = "NA"
    followers: Optional[int] = None
    following: Optional[int] = None
    admin_status: Optional[bool] = False
    admin_status_val: Optional[str] = "NA"
    


######################################################
################### Content ##########################
######################################################

class Content(BaseModel):
    content: str
    category: int
    sub_category: int
    user: int
    created_at: datetime
    updated_at: datetime
    likes: int    
    citation: Optional[str] = None
    is_public: Optional[bool] = False
    
    class Config:
        orm_mode = True
    
