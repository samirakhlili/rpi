from django.urls import path

from .views import ArticleView, InfoRspView

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('inforsp/', InfoRspView.as_view()),
]