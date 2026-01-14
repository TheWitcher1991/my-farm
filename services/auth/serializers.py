from rest_framework import serializers

from packages.kernel.adapters import ModelSerializerAdapter


class LoginSerializer(ModelSerializerAdapter):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8, max_length=100)


class RegisterSerializer(ModelSerializerAdapter):
    pass
