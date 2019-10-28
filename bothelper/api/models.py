from django.db import models
from django.utils import timezone


class TelegramUser(models.Model):
    telegram_id = models.PositiveIntegerField("Telegram ID", default=0, unique=True, null=False)
    full_name = models.CharField("Name", max_length=255, default="", null=False)
    username = models.CharField("Username", max_length=255, default="", null=True)
    phone = models.PositiveIntegerField("Phone Number", null=True, blank=True)

    language = models.CharField("Язык", max_length=5, default="RU")

    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.telegram_id)


class Photo(models.Model):
    title = models.CharField("Название", max_length=255, default="", null=False)
    photo = models.ImageField("Фото", upload_to='media/')

    def __str__(self):
        return self.title


class Room(models.Model):
    title = models.CharField("Название", max_length=255, default="", null=False)

    descriptionRU = models.TextField("Описание РУ")
    descriptionUZ = models.TextField("Описание УЗ")

    photoes = models.ManyToManyField(Photo)

    def __str__(self):
        return self.title
