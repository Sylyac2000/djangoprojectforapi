from django.urls import path
app_name = "posts"
from . import views

urlpatterns = [
    path('posts/',views.PostList.as_view(), name="post-list" ),
    path('posts/<int:pk>',views.PostDetail.as_view(), name="post-detail" ),
]