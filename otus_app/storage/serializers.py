# accounts/serializers.py

from rest_framework import serializers
from .models import Storage

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['Product_id', 'Counts_product', 'Counts_of_booking','created_at','updated_at']


