from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Message
from .serializers import UserSerializer, MessageSerializer
from django.db.models import Q


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def message_detail(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        message.is_read = True
        message.save()
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def unread_message_list(request):
    if request.method == 'GET':
        messages = Message.objects.filter(is_read=False)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def specific_user_message_list(request, pk):
    if request.method == 'GET':
        sent_or_received = request.GET.get('sent_or_received', 'all')
        if sent_or_received == 'sent':
            messages = Message.objects.filter(sender=pk)
        elif sent_or_received == 'received':
            messages = Message.objects.filter(receiver=pk)
        elif sent_or_received == 'all':
            messages = Message.objects.filter(Q(sender=pk) | Q(receiver=pk))
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def unread_specific_message_list(request, pk):
    if request.method == 'GET':
        messages = Message.objects.filter(Q(is_read=False) & Q(receiver=pk))
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
