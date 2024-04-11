from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from agrochemicals_management_system.models import CustomUser
# Register your models here.
#class model to keep password encrypted


class UserModel(UserAdmin):
    pass
admin.site.register(CustomUser, UserModel)
