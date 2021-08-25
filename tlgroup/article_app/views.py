import requests
from django.views.generic import ListView
from article_app.models import Article
from main_app.models import User, UserCompany, UserAddress


class ArticleListView(ListView):
    """Таблица постов"""
    queryset = Article.objects.all().select_related('user_id')
    template_name = 'article_app/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = 'http://jsonplaceholder.typicode.com/'
        users = requests.get(f'{url}users')
        articles = requests.get(f'{url}posts')
        if users.status_code == 200:
            User.add_user(users.json())
            UserCompany.add_user_company(users.json())
            UserAddress.add_user_address(users.json())
        if articles.status_code == 200:
            Article.add_article(articles.json())

        context['address'] = UserAddress.objects.all()
        context['title'] = 'Таблица постов'
        return context
