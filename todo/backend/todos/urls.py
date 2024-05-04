


from django.urls import path, include
from .views import TodoListAPIView, TodoRetriveAPIView

urlpatterns = [

    path('todos/', TodoListAPIView.as_view(),name="todos"),
    path('todos/<int:pk>/', TodoRetriveAPIView.as_view(), name="get_todo")
]