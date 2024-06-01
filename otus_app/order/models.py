# accounts/models.py

from django.db import models


class Orders(models.Model):
    OrderID = models.AutoField('OrderID', primary_key=True)
    UserName = models.CharField('UserName', max_length=255)
    UserID = models.IntegerField('UserID', null=True, blank=True)
    Amount = models.IntegerField('Amount', null=True, blank=True)
    Product_id = models.IntegerField('Product_id', null=True, blank=True)
    Counts_product = models.IntegerField('Counts', null=True, blank=True)
    IsPayed = models.BooleanField(default=False)
    DateTime = models.DateTimeField('DateTime', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.ID