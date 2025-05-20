from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    is_active = serializers.BooleanField(default=False)
    def validate(self, value):
        try:
            User.objects.get(username=value)
        except User.DoesNotExist:
            return value
        raise ValidationError("Username already exists")

class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

class UserConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)
    def validate(self, value):
        try:
            User.objects.get(username=value['username'])
        except User.DoesNotExist:
            raise ValidationError("User does not exist")
        return value