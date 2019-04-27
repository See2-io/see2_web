from django.conf import settings
from django.db import models


# Create your models here.
class Member(models.Model):
    '''
    A See2 Member is a registered user of See2
    '''
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    first_names = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return '{} {} {}'.format(self.title, self.first_names, self.last_name)
