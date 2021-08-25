from django.contrib import admin
from main_app.models import User, UserAddress, UserCompany

admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserCompany)
