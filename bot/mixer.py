from client import bot_models

count = bot_models.Message.objects.all().count()
for message in bot_models.Message.objects.all():
    new = bot_models.Message()

    new.text = message.text
    new.title = f" УЗ {str(message.title).replace('РУ ', '')}"
    new.number = int(message.number) + int(count)
    new.save()

    print(new.number)

