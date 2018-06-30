from django.db import models
from users.models import User
from djeet.models import Djeet


class DjeeterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    likes = models.ManyToManyField(Djeet, related_name="liked_by", symmetrical=False)

User.djeeterprofile = property(lambda u: DjeeterProfile.objects.get_or_create(user=u)[0])
