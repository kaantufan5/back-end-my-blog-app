from rest_framework import serializers, validators
from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostNowView
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'user_id',
            'post',
            'time_stamp',
            'content'
        )


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Like
        fields = (
            'id',
            'user',
            'user_id',
            'post'
        )


class PostNowViewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PostNowView
        fields = (
            'id',
            'user',
            'user_id',
            'post',
            'time_stamp',
        )


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_all = LikeSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    post_views = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    category_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'image',
            'category',
            'category_id',
            'publish_date',
            'author',
            'author_id',
            'slug',
            'comments',
            'likes',
            'likes_all',
            'post_views',
            'comment_count',
        )

    def get_likes(self, obj):
        return Like.objects.filter(post=obj).count()

    def get_post_views(self, obj):
        return PostNowView.objects.filter(post=obj).count()

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()
