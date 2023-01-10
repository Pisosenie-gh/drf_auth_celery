from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

"""Модель сообщений"""
class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"