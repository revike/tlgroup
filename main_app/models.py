from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class User(models.Model):
    """Пользователи"""
    name = models.CharField(max_length=128, blank=True)
    username = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128)
    phone = PhoneField(blank=True)
    website = models.URLField(max_length=256, blank=True)

    @staticmethod
    def add_user(users):
        for user in users:
            User(
                id=user['id'],
                name=user['name'],
                username=user['username'],
                email=user['email'],
                phone=user['phone'],
                website=user['website'],
            ).save()


class UserAddress(models.Model):
    """Адрес пользователя"""
    user = models.ForeignKey(
        User, null=False, db_index=True, on_delete=models.CASCADE,
        related_name='user_address')
    street = models.CharField(max_length=128)
    suite = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=128)
    lat = models.FloatField()
    lng = models.FloatField()

    @staticmethod
    def add_user_address(users):
        for user in users:
            UserAddress(
                id=user['id'],
                user=User.objects.filter(id=user['id']).first(),
                street=user['address']['street'],
                suite=user['address']['suite'],
                city=user['address']['city'],
                zipcode=user['address']['zipcode'],
                lat=user['address']['geo']['lat'],
                lng=user['address']['geo']['lng'],
            ).save()


class UserCompany(models.Model):
    """Компания пользователя"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, null=False,
        related_name='user_company')
    name = models.CharField(max_length=128)
    catch_phrase = models.CharField(max_length=128)
    bs = models.CharField(max_length=128)

    @staticmethod
    def add_user_company(users):
        for user in users:
            UserCompany(
                id=user['id'],
                user=User.objects.filter(id=user['id']).first(),
                name=user['company']['name'],
                catch_phrase=user['company']['catchPhrase'],
                bs=user['company']['bs']
            ).save()
