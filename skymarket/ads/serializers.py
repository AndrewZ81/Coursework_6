from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.fields import SerializerMethodField

from .models import Ad, Comment

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


class CommentListViewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(allow_blank=False, allow_null=False)
    ad_id = SerializerMethodField(required=False)
    author_id = SerializerMethodField(required=False)
    author_first_name = SerializerMethodField()
    author_last_name = SerializerMethodField()
    author_image = SerializerMethodField()


    class Meta:
        model = Comment
        exclude = ["ad", "author"]

    def get_text(self, comment):
        return comment.text

    def get_ad_id(self, comment):
        return comment.ad_id

    def get_author_id(self, comment):
        return comment.author_id

    def get_author_first_name(self, comment):
        return comment.author.first_name

    def get_author_last_name(self, comment):
        return comment.author.last_name

    def get_author_image(self, comment):
        return comment.author.image.url if comment.author.image else None
