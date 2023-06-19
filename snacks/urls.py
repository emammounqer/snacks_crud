from django.urls import path
from .views import SnackListView

urlpatterns = [
    path('snacks', SnackListView.as_view(), name='snack_list')
]
