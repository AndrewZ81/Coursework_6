from rest_framework import serializers

from .models import Ad


class AdListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ["author", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass
