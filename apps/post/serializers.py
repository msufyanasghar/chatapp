from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth import get_user_model

User = get_user_model()

class PostViewSerializer(serializers.ModelSerializer):
    
    likes = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'description', 'date_posted', 'image', 'likes','author']
        
    def get_likes(self, obj : Post):
        return obj.likers.count()
    

class PostCreateSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model = Post
        fields = ['description', 'image']
        
    def create(self, validated_data):
        print("************************\n\n\n")
        print(self.context['request'].data)
        print(self.context['request'].user)
        print("************************\n\n\n")
        
        token = f'{self.context['request'].user}'.strip(' ')[-1]
        user_id = int(token)
        user = User.objects.get(id=user_id)
        
        return Post.objects.create(
            author = user,
            **validated_data
        )