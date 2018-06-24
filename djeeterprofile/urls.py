from django.urls import path, include

from .views import (
    frontpage, signout, follows, followers, follow, stopfollow, profile,
    ProfileView
)


app_name = "djeeterprofile"

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("signout/", signout, name="signout"),
    path("<str:username>/follows/", follows, name="follows"),
    path("<str:username>/following/", followers, name="following"),
    path("<str:username>/follow/", follow, name="follow"),
    path("<str:username>/stopfollow/", stopfollow, name="stopfollow"),
    path("<str:username>/", ProfileView.as_view(), name="profile"),
]
