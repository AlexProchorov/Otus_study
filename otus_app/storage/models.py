# accounts/models.py

from django.db import models


class Storage(models.Model):
    RawID = models.AutoField('ID', primary_key=True)
    Product_id = models.IntegerField('Product_id', null=True, blank=True)
    Counts_product = models.IntegerField('Counts_product', null=True, blank=True)
    Is_booking = models.BooleanField(default=False)
    User_id = models.IntegerField('UserID', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      # Add custom fields here, if needed

    def __str__(self):
        return self.Product_id