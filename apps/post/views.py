from django.shortcuts import render
from rest_framework import (generics, permissions, authentication)
from .models import *
from .serializers import *
# Create your views here.


class PostCreateApiView(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return PostViewSerializer
        else:
            return  PostCreateSerializer
    
    
    def post(self, request, *args, **kwargs):
        print("************************\n\n\n")
        print(request.data)
        print(request.FILES)
        print("************************\n\n\n")
        return super().post(request, *args, **kwargs)
        
    # def perform_create(self, serializer):
    #     print("************************\n\n\n")
    #     print(self.request.data)
    #     print("************************\n\n\n")
    #     serializer.save(author=self.request.user)
    
    def get_serializer_context(self):
        return {'request': self.request}
