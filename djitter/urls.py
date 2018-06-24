from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from djeeterprofile.views import frontpage, signout, profile, follows, followers, follow, stopfollow
from djeet.views import feed


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", frontpage, name="frontpage"),
    path("signout/", signout, name="signout"),
    path("feed/", feed, name="feed"),
    path("<str:username>/follows/", follows, name="follows"),
    path("<str:username>/following/", followers, name="following"),
    path("<str:username>/follow/", follow, name="follow"),
    path("<str:username>/stopfollow/", stopfollow, name="stopfollow"),
    path("<str:username>/", profile, name="profile"),
]
