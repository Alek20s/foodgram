from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name')
    search_fields = ('email', 'username')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Avatar', {'fields': ('avatar',)}),
    )


admin.site.unregister(Group)
admin.site.unregister(Token)
