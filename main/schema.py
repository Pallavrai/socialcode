from ninja import ModelSchema
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Like, Follow


class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ProfileSchema(ModelSchema):
    user: UserSchema 

    class Config:
        model = Profile
        model_fields = ['id', 'user', 'bio', 'profile_pic']


class PostSchema(ModelSchema):
    author: UserSchema  

    class Config:
        model = Post
        model_fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'image']


class CommentSchema(ModelSchema):
    post: PostSchema 
    author: UserSchema  

    class Config:
        model = Comment
        model_fields = ['id', 'post', 'author', 'content', 'created_at']


class LikeSchema(ModelSchema):
    post: PostSchema  
    user: UserSchema  

    class Config:
        model = Like
        model_fields = ['id', 'post', 'user', 'created_at']


class FollowSchema(ModelSchema):
    follower: UserSchema  
    following: UserSchema 

    class Config:
        model = Follow
        model_fields = ['id', 'follower', 'following', 'created_at']
