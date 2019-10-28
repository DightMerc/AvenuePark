from django.contrib import admin
from .models import TelegramUser, Photo, Room

# Register your models here.

admin.site.register(TelegramUser)
admin.site.register(Photo)
admin.site.register(Room)

