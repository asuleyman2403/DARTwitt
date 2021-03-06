from rest_framework import serializers
from homepage.serializers import ProfileSerializer
from post.models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    created_at = serializers.DateTimeField(required=False)
    repost = ProfileSerializer(required=False)
    owner = ProfileSerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False)
    owner = ProfileSerializer(required=False)
    post = PostSerializer(required=False)

    class Meta:
        model = Comment
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class LikeSerializer(serializers.ModelSerializer):
    post = PostSerializer(required=False)
    # comment = CommentSerializer(required=False)
    owner = ProfileSerializer(required=False)

    class Meta:
        model = Like
        fields = '__all__'
