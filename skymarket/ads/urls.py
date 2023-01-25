from django.urls import include, path
from .views import AdListView, AdDetailView, AdMyListView

urlpatterns = [
    path('', AdListView.as_view(), name="ads_list"),
    path('<int:pk>/', AdDetailView.as_view(), name="ad_detail"),
    path('me/', AdMyListView.as_view(), name="my_ads_list")
]
