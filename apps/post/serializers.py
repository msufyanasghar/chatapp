from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth import get_user_model

User = get_user_model()

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
    
    # def get_auth
    

class PostCreateSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model = Post
        fields = ['description', 'image']
        
    def create(self, validated_data):
        
        token = f'{self.context['request'].user}'.strip(' ')[-1]
        user_id = int(token)
        user = User.objects.get(id=user_id)
        
        return Post.objects.create(
            author = user,
            **validated_data
        )