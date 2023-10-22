from pydantic import BaseModel
from typing import Optional

#######################################################
################# UserAuth ###########################
#######################################################

class UserForAuthBase(BaseModel):
    name: str
    email: str
    password: str
    is_disabled: bool

class UserForAuthUpdate(UserForAuthBase):
    pass


#######################################################
################# User ###############################
#######################################################
class UserBase(BaseModel):
    user_id: int
    phone: str
    profile_pic: Optional[str]
    birth_date: str
    gender: str
    bio: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    twitter_id: Optional[str]
    instagaram_id: str
    followers: int
    following: int
    admin_status: bool
    admin_status_val: str

class UserUpdate(UserBase):
    pass


#######################################################
################# Content ############################
#######################################################
class ContentBase(BaseModel):
    content: str
    category: int
    sub_category: int
    user: int
    citation: Optional[str]
    is_public: bool

class ContentUpdate(ContentBase):
    pass


#######################################################
################# Comments ############################
#######################################################

class CommentsBase(BaseModel):
    comment_content: str
    comment_likes: int
    comment_user: int
    flag_is_updated: bool
    flag_show: bool
    flag_comment_of_comment: bool

class CommentsUpdate(CommentsBase):
    pass


#######################################################
################# Content_comment #####################
#######################################################

class ContentCommentBase(BaseModel):
    content_id: int
    comment_id: int

class ContentCommentUpdate(ContentCommentBase):
    pass


#######################################################
################# Comment_comment #####################
#######################################################

class CommentCommentBase(BaseModel):
    head_comment_id: int
    reply_comment_id: int

class CommentCommentUpdate(CommentCommentBase):
    pass


#######################################################
################# Category ############################


class CategoryBase(BaseModel):
    category_name: str
    category_description: str
    category_pic: Optional[str]

class CategoryUpdate(CategoryBase):
    pass


#######################################################
################# Sub_Category ########################
#######################################################

class SubCategoryBase(BaseModel):
    sub_category_name: str
    sub_category_description: str
    sub_category_pic: Optional[str]
    category_id: int

class SubCategoryUpdate(SubCategoryBase):
    pass


#######################################################
################# Collection #########################
#######################################################

class CollectionBase(BaseModel):
    collection_name: str
    collection_description: str
    collection_user: int
    collection_posts: int

class CollectionUpdate(CollectionBase):
    pass


#######################################################
################# Content_collection ##################
#######################################################

class BookmarkBase(BaseModel):
    bookmark_user: int
    bookmark_content: int

class BookmarkUpdate(BookmarkBase):
    pass
