from rest_framework import serializers
from .models import *


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