from django.shortcuts import render
from rest_framework.response import Response
from helloworld.serializers import PostSerializer
from rest_framework.views import APIView  
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from helloworld.permissions import IsPostpossessor 
from rest_framework import filters as filter
from helloworld.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})


class PostViewSet(ModelViewSet):
    permission_classes = [IsPostpossessor]
     
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filter.SearchFilter,filter.OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'content']
    filter_class = PostFilter
    ordering_fields = ['id']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(created_by=self.request.user)
        return Post.objects.none()
    