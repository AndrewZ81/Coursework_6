from django.urls import path
from .views import AdMyListView, AdListCreateView, AdRetrieveUpdateDestroyView

urlpatterns = [
    path('', AdListCreateView.as_view(), name="ads_list"),
    path('<int:pk>/', AdRetrieveUpdateDestroyView.as_view(), name="ad_rud"),
    path('me/', AdMyListView.as_view(), name="my_ads_list"),

]
