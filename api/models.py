from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.utils import timezone
# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Person(AbstractUser, models.Model):
    profile_pic = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=5000, blank=True)
    date = models.DateTimeField(default=timezone.now)
    image = models.TextField(blank=True)
    board = models.ForeignKey(
        Board, related_name="posts", on_delete=models.CASCADE)
    author = models.ForeignKey(
        Person, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    content = models.TextField(max_length=1000, blank=True)
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        Person, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-date']
