from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from djeeterprofile.views import frontpage, signout, profile
from djeet.views import feed


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", frontpage, name="frontpage"),
    path("signout/", signout, name="signout"),
    path("feed/", feed, name="feed"),
    path("<str:username>/", profile, name="profile"),
]

