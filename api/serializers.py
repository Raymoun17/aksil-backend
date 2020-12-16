from .models import Board, Person, Post, Comment
from rest_framework import serializers


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'url', 'name', 'posts', ]


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'url', 'username', 'profile_pic', 'posts', 'comments']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'content', 'date',
                  'image', 'board', 'author', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'url', 'content', 'date', 'post', 'author']
