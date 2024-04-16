from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

def get_user_id(request):
    token = f'{request.user}'.strip(' ')[-1]
    user_id = int(token)
    return user_id
    
class PostViewSerializer(serializers.ModelSerializer):
    
    likes = serializers.SerializerMethodField()
    
    author = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'description', 'date_posted', 'image', 'likes','author']
        
    def get_author(self, obj:Post):
        return f'{obj.author.first_name} {obj.author.last_name}'
        
    def get_likes(self, obj : Post):
        return obj.likers.count()


class PostCreateSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Post
        fields = ['description', 'image']
        
    def create(self, validated_data):
        
        user_id = get_user_id(self.context['request'])
        
        user = User.objects.get(id=user_id)
        
        return Post.objects.create(
            author = user,
            **validated_data
        )
        
class LikeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    
    def validate_id(self, val):
        
        if Post.objects.filter(id = val).exists():
            return val
        else:
            raise serializers.ValidationError("This Post does not exists.")
        

# class CommentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'post', 'date_posted']
