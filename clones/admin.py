from django.contrib import admin

from .models import Event, Category, Item, Post

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Post)
