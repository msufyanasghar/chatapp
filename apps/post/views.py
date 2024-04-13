from django.shortcuts import render
from rest_framework import (generics, permissions, authentication)
from .models import *
from .serializers import *
# Create your views here.


class PostCreateApiView(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return PostViewSerializer
        else:
            return  PostCreateSerializer
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
