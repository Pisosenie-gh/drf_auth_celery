from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .serializers import TelegramToken, ChatId
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer, MyMessageSerializer
from .models import Message
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .services import send
import uuid


User = get_user_model()


"""Отправка сообщений"""
class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message_serializer = MessageSerializer(data=request.data)

        if message_serializer.is_valid():
            message = message_serializer.save(user=request.user)
            text = f"{request.user.username}, я получил от тебя сообщение:\n{message.text}"
            send(request.user.chat_id, text)
            return Response(message_serializer.data, status=status.HTTP_201_CREATED)
        return Response(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



"""Получние токена"""
@api_view(['GET'])
def get_token(request):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.get(id=int(request.user.id))
    return Response({"token": queryset.telegram_token})

"""Записаь чат-айди (для бота)"""
class ChatView(APIView):

    def get_object(self, token):
        return User.objects.get(telegram_token=token)

    def patch(self, request, token):
        model_object = self.get_object(token)
        serializer = ChatId(model_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)


"""Генерация токена"""
class GenerateTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        return User.objects.get(id=int(request.user.id))

    def patch(self, request):
        model_object = self.get_object(request)
        serializer = TelegramToken(model_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(telegram_token=uuid.uuid4())
            return JsonResponse(data=serializer.data)


"""Получение своих сообщений"""
@api_view(['GET'])
def get_messages(request):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all().filter(user=request.user.id)
    serializer = MyMessageSerializer(queryset, many=True)
    return Response(serializer.data)

