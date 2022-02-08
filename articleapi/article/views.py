from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Author
from .serializers import ArticleSerializer
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# Create your views here.

# return a list of all articles that we currently have in our database
# class ArticleView(ListModelMixin, GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)

# Provide user with ability to create and article
# class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def perform_create(self, serializer):
#         author = get_object_or_404(Author, id=self.request.data.get('author_id'))
#         return serializer.save(author=author)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# without the need to define get and post
# class ArticleView(CreateAPIView, ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def perform_create(self, serializer):
#         author = get_object_or_404(Author, id=self.request.data.get('author_id'))
#         return serializer.save(author=author)

# Combining both creating and listing an article
class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

# This allows only to view single article using article id
# class SingleArticleView(RetrieveAPIView):  # to allow users to update their articles, provide user with a way to retrieve a single article
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# This allows us to retrieve the article using id and at the same time update the article 
class SingleArticleView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer