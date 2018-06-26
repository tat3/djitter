from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

from .views import page_not_found


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("djeet.urls", namespace="djeet")),
    path("", include("djeeterprofile.urls", namespace="profile")),
]

