from rest_framework import serializers
from .models import Message
from .models import Setting
from .models import PaySystem



class MessageSerializer(serializers.Serializer):
    title = serializers.CharField()
    number = serializers.IntegerField()
    text = serializers.CharField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ('title', 'token', 'paysystem')

    def create(self, validated_data):
        paysystems = validated_data.pop('paysystem')
        instance = Order.objects.create(**validated_data)
        for paysystem in paysystems:
            instance.paysystem.add(paysystem)

        return instance

class PaySystemSerializer(serializers.Serializer):
    title = serializers.CharField()
    token = serializers.CharField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)


     