# accounts/serializers.py

from rest_framework import serializers
from .models import Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['OrderID', 'UserName', 'UserID','Amount','IsPayed']

    def update (self,instance,validate_date):
        instance.IsPayed = validate_date.get('IsPayed',instance.IsPayed)
        instance.save()
        return instance
