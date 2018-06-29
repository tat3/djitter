from django.db import models
from users.models import User


class DjeeterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.djeeterprofile = property(lambda u: DjeeterProfile.objects.get_or_create(user=u)[0])
