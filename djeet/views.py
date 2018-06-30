from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Djeet


class FeedView(TemplateView):
    template_name = "djeet/djeets.html"

    def get(self, request):
        userids = [item.id for item in request.user.djeeterprofile.follows.all()]
        userids.append(request.user.id)
        djeets = list(Djeet.objects.filter(user_id__in=userids)[:25])
        return self.render_to_response({
            "title": "Feed",
            "djeets": djeets
        })

