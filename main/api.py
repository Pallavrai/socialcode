from typing import List
from ninja import NinjaAPI
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile, Post, Comment, Like, Follow
from .schema import ProfileSchema, PostSchema, CommentSchema, LikeSchema, FollowSchema, UserSchema

api = NinjaAPI()

# Profile endpoints
@api.get("/profiles", response=List[ProfileSchema])
def list_profiles(request):
    return Profile.objects.select_related('user').all()

@api.get("/profiles/{profile_id}", response=ProfileSchema)
def get_profile(request, profile_id: int):
    profile = get_object_or_404(Profile, id=profile_id)
    return profile

@api.post("/profiles", response=ProfileSchema)
def create_profile(request, payload: ProfileSchema):
    profile = Profile.objects.create(**payload.dict(exclude_unset=True))
    return profile

@api.put("/profiles/{profile_id}", response=ProfileSchema)
def update_profile(request, profile_id: int, payload: ProfileSchema):
    profile = get_object_or_404(Profile, id=profile_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(profile, attr, value)
    profile.save()
    return profile

@api.delete("/profiles/{profile_id}")
def delete_profile(request, profile_id: int):
    profile = get_object_or_404(Profile, id=profile_id)
    profile.delete()
    return {"success": True}

# Post endpoints
@api.get("/posts", response=List[PostSchema])
def list_posts(request):
    return Post.objects.select_related('author').all()

@api.get("/posts/{post_id}", response=PostSchema)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post

@api.post("/posts", response=PostSchema)
def create_post(request, payload: PostSchema):
    post = Post.objects.create(**payload.dict(exclude_unset=True))
    return post

@api.put("/posts/{post_id}", response=PostSchema)
def update_post(request, post_id: int, payload: PostSchema):
    post = get_object_or_404(Post, id=post_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(post, attr, value)
    post.save()
    return post

@api.delete("/posts/{post_id}")
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return {"success": True}

# Comment endpoints
@api.get("/comments", response=List[CommentSchema])
def list_comments(request):
    return Comment.objects.select_related('post', 'author').all()

@api.get("/comments/{comment_id}", response=CommentSchema)
def get_comment(request, comment_id: int):
    comment = get_object_or_404(Comment, id=comment_id)
    return comment

@api.post("/comments", response=CommentSchema)
def create_comment(request, payload: CommentSchema):
    comment = Comment.objects.create(**payload.dict(exclude_unset=True))
    return comment

@api.put("/comments/{comment_id}", response=CommentSchema)
def update_comment(request, comment_id: int, payload: CommentSchema):
    comment = get_object_or_404(Comment, id=comment_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(comment, attr, value)
    comment.save()
    return comment

@api.delete("/comments/{comment_id}")
def delete_comment(request, comment_id: int):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return {"success": True}

# Like endpoints
@api.get("/likes", response=List[LikeSchema])
def list_likes(request):
    return Like.objects.select_related('post', 'user').all()

@api.get("/likes/{like_id}", response=LikeSchema)
def get_like(request, like_id: int):
    like = get_object_or_404(Like, id=like_id)
    return like

@api.post("/likes", response=LikeSchema)
def create_like(request, payload: LikeSchema):
    like = Like.objects.create(**payload.dict(exclude_unset=True))
    return like

@api.delete("/likes/{like_id}")
def delete_like(request, like_id: int):
    like = get_object_or_404(Like, id=like_id)
    like.delete()
    return {"success": True}

# Follow endpoints
@api.get("/follows", response=List[FollowSchema])
def list_follows(request):
    return Follow.objects.select_related('follower', 'following').all()

@api.get("/follows/{follow_id}", response=FollowSchema)
def get_follow(request, follow_id: int):
    follow = get_object_or_404(Follow, id=follow_id)
    return follow

@api.post("/follows", response=FollowSchema)
def create_follow(request, payload: FollowSchema):
    follow = Follow.objects.create(**payload.dict(exclude_unset=True))
    return follow

@api.delete("/follows/{follow_id}")
def delete_follow(request, follow_id: int):
    follow = get_object_or_404(Follow, id=follow_id)
    follow.delete()
    return {"success": True}
