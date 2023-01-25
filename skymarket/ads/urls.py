from django.urls import include, path
from .views import AdListView, AdDetailView, AdMyListView, AdCreateView

urlpatterns = [
    path('', AdListView.as_view(), name="ads_list"),
    path('create/', AdCreateView.as_view(), name="ad_create"),
    path('<int:pk>/', AdDetailView.as_view(), name="ad_detail"),
    path('me/', AdMyListView.as_view(), name="my_ads_list"),

]
