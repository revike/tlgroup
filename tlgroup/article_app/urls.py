from django.urls import path
from article_app.views import ArticleListView

app_name = 'article_app'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article')
]
