from django.db import models

from main_app.models import User


class Article(models.Model):
    """Посты"""
    user_id = models.ForeignKey(
        User, null=False, db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.TextField()

    @staticmethod
    def add_article(articles):
        for article in articles:
            Article(
                id=article['id'],
                user_id=User.objects.filter(id=article['userId']).first(),
                title=article['title'],
                body=article['body'],
            ).save()
