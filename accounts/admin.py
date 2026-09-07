from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Scrapify", {"fields": ("phone", "role")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Scrapify", {"fields": ("phone", "role")}),)
    list_display = ("username", "email", "phone", "role", "is_staff")
