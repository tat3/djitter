from django.shortcuts import render

from .models import Djeet


def feed(request):
    userids = [id_ for id_ in request.user.djeeterprofile.follows.all()]

    userids.append(request.user.id)
    djeets = list(Djeet.objects.filter(user_id__in=userids))[:25]

    return render(request, "djitter/feed.html", {"djeets": djeets})

