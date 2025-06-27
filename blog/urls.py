from django.urls import path
from .views import ListCreatePost, RetrievePost, Authors


urlpatterns = [
    path("", ListCreatePost.as_view()),
    path("<int:pk>/", RetrievePost.as_view()),
    path("authors/", Authors.as_view()),
]