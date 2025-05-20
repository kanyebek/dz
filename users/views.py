from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, UserAuthSerializer
from .models import ConfirmationCode

# Create your views here.

@api_view(['POST'])
def register(request):
    if request.method =='POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        is_active = serializer.validated_data['is_active']
        user = User.objects.create_user(username=username, password=password, is_active=is_active)
        user.save()
        confirmation = ConfirmationCode(user=user)
        confirmation.save()
        return Response({"message": "User created successfully", 
                         "confirmation_code": confirmation.code}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def confirm_user(request):
    username = request.data.get('username')
    code = request.data.get('code')

    try:
        user = User.objects.get(username=username)
        confirmation = ConfirmationCode.objects.get(user=user)
    except (User.DoesNotExist, ConfirmationCode.DoesNotExist):
        return Response({"error": "Invalid username or confirmation code"}, status=status.HTTP_400_BAD_REQUEST)

    if confirmation.code == code:
        user.is_active = True
        user.save()
        confirmation.delete() 
        return Response({"message": "User confirmed successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Incorrect confirmation code"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

