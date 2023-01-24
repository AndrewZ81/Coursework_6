from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):

    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data["password"])
        new_user.save()
        return new_user

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "email", "password", "image"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "phone", "email", "image"]
