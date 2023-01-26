from django.urls import path
from .views import AdMyListView, AdListCreateView, AdRetrieveUpdateDestroyView, \
    CommentListCreateView, CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('', AdListCreateView.as_view(), name="ads_list"),
    path('<int:pk>/', AdRetrieveUpdateDestroyView.as_view(), name="ad_read_upd_del"),
    path('me/', AdMyListView.as_view(), name="my_ads_list"),
    path('<int:ad_pk>/comments/', CommentListCreateView.as_view(), name="comment_list_create"),
    path('comments/<int:pk>', CommentRetrieveUpdateDestroyView.as_view(), name="comment_read_upd_del")

]
