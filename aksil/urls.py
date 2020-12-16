from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import BoardViewSet, PersonViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('boards', BoardViewSet)
router.register('users', PersonViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
