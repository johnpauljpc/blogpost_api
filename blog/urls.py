from django.urls import path
from .views import ListCreatePost, RetrievePost


urlpatterns = [
    path("", ListCreatePost.as_view()),
    path("<int:pk>/", RetrievePost.as_view()),
]