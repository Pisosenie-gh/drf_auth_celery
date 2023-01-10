from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'text')


"""Сериализатор сообщений"""
class MyMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'text', 'user', 'date')


"""Сериализатор токена"""
class TelegramToken(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('telegram_token',)

"""Сериализатор чат-айди(для бота)"""
class ChatId(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('chat_id',)

