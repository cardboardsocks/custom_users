from django.contrib import admin
from myuser.models import MyUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser, UserAdmin)
# Register your models here.
