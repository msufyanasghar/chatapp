from django.shortcuts import render
from rest_framework import (generics, permissions, authentication, status)
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import *
# Create your views here.


class PostListCreateApiView(generics.ListCreateAPIView):
    
    queryset = Post.objects.prefetch_related('author').prefetch_related('comment_set').all()
    
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
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

class LikeApiView(APIView):
    
    """
    will require post id 
    """
    
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        
        # print("Post method trigerred ++++++++++++++++++++++++++")
        # print(self.request.data)
        # print("Post method trigerred ++++++++++++++++++++++++++")
        
        data = LikeSerializer(data = request.data)
        
        if data.is_valid(raise_exception=True):
            
            post = Post.objects.get(id = data.data['id'])
            
            all_likers = post.likers.all()
            
            user = User.objects.get(id = get_user_id(request))
            
            if user in all_likers:
                post.likers.remove(user)
            else:
                post.likers.add(user)
                
            post.save()
            
            return Response({},status=status.HTTP_200_OK)
        
        return Response({"message": "Hello, world!"})
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    
class DeletePost(APIView):
    
    permission_classes = [permissions.IsAuthenticated, IsOwnerPermission]
    queryset = Post.objects.prefetch_related('author').all()
    
    def delete(self, request):
        data = LikeSerializer(data = request.data)
        
        if data.is_valid(raise_exception=True):
            
            d = Post.objects.get(id = data.data['id']).delete()
        
        return Response({"message": "Done"})
