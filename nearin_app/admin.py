from typing import Type
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Shop_login)
admin.site.register(Shop_profile)
admin.site.register(Master)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(Shop_type)
admin.site.register(State)
admin.site.register(City)