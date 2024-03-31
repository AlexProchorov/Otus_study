from django.db.models import fields
from rest_framework import serializers
from .models import Users_info


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_info
        fields = ('ID','UserName', 'FirstName', 'LastName', 'Email', 'Phone')



