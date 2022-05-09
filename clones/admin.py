from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Event, Category, Item, Post, Photo, CustomUser

class CustomUserAdmin(UserAdmin):    
    model = CustomUser
    list_display = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Post)
admin.site.register(Photo)
