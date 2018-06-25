from django.urls import path
from django.views.generic.base import TemplateView

from .views import FeedView


app_name = "djeet"

urlpatterns = [
    path("feed/", FeedView.as_view(), name="feed"),
]
