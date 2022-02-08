from django.urls import path

from .views import ArticleView

app_name = 'article'

# app_name will help us do a reverse look-up later

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]