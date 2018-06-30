from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core import validators


class User(AbstractUser):
    nickname = models.CharField(max_length=10, default="unknown")
    username = models.CharField(_('username'), max_length=10, unique=True,
        help_text=_('Required. 10 characters or fewer. Letters, digits and '
                    '_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and _ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    profile = models.CharField(max_length=140, default="")

