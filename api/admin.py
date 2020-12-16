from django.contrib import admin
from .models import Board, Person, Post, Comment
# Register your models here.
admin.site.register(Board)
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Comment)
