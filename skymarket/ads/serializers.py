from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.relations import SlugRelatedField, PrimaryKeyRelatedField
from rest_framework.fields import SerializerMethodField

from .models import Ad

User = get_user_model()


class AdListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ["author", "created_at"]


class AdDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ["created_at", "author"]

    author_id = PrimaryKeyRelatedField(queryset=User.objects.all())
    author_first_name = SerializerMethodField()
    author_last_name = SerializerMethodField()
    phone = SerializerMethodField()


    def get_author_first_name(self, ad):
        return ad.author.first_name

    def get_author_last_name(self, ad):
        return ad.author.last_name

    def get_phone(self, ad):
        return str(ad.author.phone)


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass
