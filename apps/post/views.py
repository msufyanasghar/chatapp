from django.shortcuts import render
from rest_framework import (generics, permissions, authentication)
from .models import *
from .serializers import *
# Create your views here.


class PostCreateApiView(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    
    def get_permissions(self):
        if self.request.method=='GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAuthenticated()]
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return PostViewSerializer
        else:
            return  PostCreateSerializer
        
        
    def get_serializer_context(self):
        return {'request': self.request}
