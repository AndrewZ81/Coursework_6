from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.relations import PrimaryKeyRelatedField
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

    author_id = SerializerMethodField(required=False)
    author_first_name = SerializerMethodField()
    author_last_name = SerializerMethodField()
    phone = SerializerMethodField()

    def get_author_id(self, ad):
        return ad.author_id

    def get_author_first_name(self, ad):
        return ad.author.first_name

    def get_author_last_name(self, ad):
        return ad.author.last_name

    def get_phone(self, ad):
        return str(ad.author.phone)
