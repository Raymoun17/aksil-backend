from .models import Board, Comment, Person, Post
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BoardSerializer, PersonSerializer, PostSerializer, CommentSerializer


# Create your views here.
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
