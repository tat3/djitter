from django.shortcuts import render

from .models import Djeet


def feed(request):
    userids = [item.id for item in request.user.djeeterprofile.follows.all()]

    userids.append(request.user.id)
    djeets = list(Djeet.objects.filter(user_id__in=userids)[:25])

    return render(request, "djeet/feed.html", {"djeets": djeets})

