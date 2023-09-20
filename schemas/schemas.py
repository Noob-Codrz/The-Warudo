

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
    
class UserDB(User):
    hashed_password: str
    
class UserDetails(User):
    # phone = Column(String(10), unique=True)
    # profile_pic = Column(String(100)) ## store in s3
    # created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # birth_date = Column(DateTime)
    # gender = Column(String(10))
    # bio = Column(Text)
    # city = Column(String(100))
    # state = Column(String(100))
    # country = Column(String(100))
    # twitter_id = Column(String(100))
    # instagaram_id = Column(String(100), default="NA")
    # followers = Column(Integer, ForeignKey("user.id"))
    # following = Column(Integer, ForeignKey("user.id"))
    # admin_status = Column(Boolean, default=False)
    # admin_status_val = Column(String(100), default="NA")
    pass


######################################################
################### Content ##########################
######################################################

class Content(BaseModel):
    content: str
    category: str
    sub_category: str
    citation: str
    user = int
    created_at = 
    updated_at= 
    likes = int 
    
    is_public: bool
