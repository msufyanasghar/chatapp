from django.urls import path
from . import views 


urlpatterns = [
    path('feed/', views.PostCreateApiView.as_view(), name="blog_home"),
    path('create/post/', views.PostCreateApiView.as_view(), name="create_post"),
    # path('post/like/', views.like, name="like_post"),
    # path('post/delete/', views.delete, name="delete_post"),
]   