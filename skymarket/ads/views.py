from rest_framework.generics import ListAPIView, ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import AdRetrieveUpdateDestroyPermission

from .models import Ad, Comment
from .serializers import AdListViewSerializer, AdDetailViewSerializer, CommentListViewSerializer


class AdListCreateView(ListCreateAPIView):
    """
    - GET кратко отображает все объявления
    - POST создаёт новое объявление
    """
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_authenticated and self.request.method == "POST":
            return AdDetailViewSerializer
        return AdListViewSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdMyListView(ListAPIView):
    """
    Кратко отображает объявления текущего пользователя
    """
    def get_queryset(self):
        return Ad.objects.filter(author_id=self.request.user.id)
    serializer_class = AdListViewSerializer
    permission_classes = [IsAuthenticated]


class AdRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    - GET подробно отображает объявление по его id
    - PUT (PATCH) обновляет объявление по его id
    - DELETE удаляет объявление по его id
    """
    queryset = Ad.objects.all()
    serializer_class = AdDetailViewSerializer
    permission_classes = [IsAuthenticated, AdRetrieveUpdateDestroyPermission]


class CommentListCreateView(ListCreateAPIView):
    """
    - GET отображает все комментарии к объявлению, выбранному по id
    - POST создаёт новый комментарий к объявлению, выбранному по id
    """
    serializer_class = CommentListViewSerializer
    permission_classes = [IsAuthenticated]

    def get_ad_pk(self):
        return self.kwargs["ad_pk"]

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.get_ad_pk())

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.get_ad_pk())
