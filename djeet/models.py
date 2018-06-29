from django.db import models
from users.models import User

class Djeet(models.Model):
  user = models.ForeignKey(User, related_name='djeets', on_delete=models.DO_NOTHING)
  body = models.CharField(max_length=140)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created_at',)
