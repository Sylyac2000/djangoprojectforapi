from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from .views import UserViewSet

router = SimpleRouter()

router.register('users', UserViewSet, basename="users")

app_name = "posts"
urlpatterns = [
    path('posts/',views.PostList.as_view(), name="post-list" ),
    path('posts/<int:pk>',views.PostDetail.as_view(), name="post-detail" ),
]

urlpatterns += router.urls