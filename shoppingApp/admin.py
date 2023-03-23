from django.contrib import admin
from shoppingApp.models import *
from django.contrib import auth
# Register your models here.

admin.site.register(Product)
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)