from django.shortcuts import render, get_object_or_404

from .models import Message, Setting, PaySystem

from .serializers import MessageSerializer, SettingSerializer, PaySystemSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.db import IntegrityError

class ListMessageView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        
        serializer = MessageSerializer(messages, many=True)
        return Response({"messages": serializer.data})

class ListSettingView(APIView):
    def get(self, request):
        settings = Setting.objects.all()
        
        serializer = SettingSerializer(settings, many=True)
        return Response({"settings": serializer.data})

class ListPaySystemView(APIView):
    def get(self, request):
        paysystems = PaySystem.objects.all()
        
        serializer = PaySystemSerializer(paysystems, many=True)
        return Response({"paysystems": serializer.data})
    


