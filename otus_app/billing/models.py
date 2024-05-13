# accounts/models.py

from django.db import models


class Billing(models.Model):
    ID = models.AutoField('ID', primary_key=True)
    UserName = models.CharField('UserName', max_length=255)
    SumCount = models.IntegerField ('Sum', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Message = models.CharField('Message', max_length=255,null=True, blank=True)
    # Add custom fields here, if needed

    def __str__(self):
        return self.ID