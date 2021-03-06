from django.urls import path, include
from django.conf.urls import handler404


from .views import (
    ProfileView, FrontPageView, SignoutView, FollowsView, FollowersView,
    FollowView, StopFollowView, LikeView, StopLikeView, LikesView,
)


app_name = "djeeterprofile"

urlpatterns = [
    path("", FrontPageView.as_view(), name="frontpage"),
    path("signout/", SignoutView.as_view(), name="signout"),
    path("<str:username>/follows/", FollowsView.as_view(), name="follows"),
    path("<str:username>/following/", FollowersView.as_view(), name="following"),
    path("<str:username>/follow/", FollowView.as_view(), name="follow"),
    path("<str:username>/stopfollow/", StopFollowView.as_view(), name="stopfollow"),
    path("like/<str:djeet_id>/", LikeView.as_view(), name="like"),
    path("stoplike/<str:djeet_id>/", StopLikeView.as_view(), name="stoplike"),
    path("<str:username>/likes/", LikesView.as_view(), name="likes"),
    path("<str:username>/", ProfileView.as_view(), name="profile"),
]

handler404 = 'djeeterprofile.views.page_not_found'

