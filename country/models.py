from django.db import models
from authentication.models import Account
# Create your models here.


class Country(models.Model):
    name = models.TextField()
    created_by = models.ForeignKey(Account)
    dial_code = models.TextField()
    region = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return '{0}'.format(self.name)