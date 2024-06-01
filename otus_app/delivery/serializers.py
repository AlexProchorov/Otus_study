# accounts/serializers.py

from rest_framework import serializers
from .models import Delivery

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['OrderID', 'UserName', 'UserID','Product_id','DateTime']


