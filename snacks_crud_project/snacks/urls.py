from django.urls import path
from .views import (
    SnackCreateView,
    SnackDetailView,
    SnackListView,
    SnackUpdateView,
    SnackDeleteView
)

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/',SnackDetailView.as_view(),name='snack_detail'),
    path("create/",SnackCreateView.as_view(),name="snack_create"),
    path('update-thing/<int:pk>', SnackUpdateView.as_view(),name='snack_update'),
    path('delete-snack/<int:pk>', SnackDeleteView.as_view(),name='snack_delete')
]
