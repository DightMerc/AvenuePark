from django.contrib import admin
from .models import Message, PaySystem, Setting

# Register your models here.
admin.site.register(Message)
admin.site.register(PaySystem)
admin.site.register(Setting)
