from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Ad, Comment
from .serializers import AdListViewSerializer


class AdListView(ListAPIView):
    """
    Отображает таблицу Объявления
    """
    queryset = Ad.objects.all()
    serializer_class = AdListViewSerializer



class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass

