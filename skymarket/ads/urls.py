from django.urls import include, path
from .views import AdListView

urlpatterns = [
    path('', AdListView.as_view(), name="ads_list"),
]
