# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser
from api.models import Users_info


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        model_u = Users_info
        fields_u = ['UserName', 'email']


    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        user_info = Users_info(
            UserName = validated_data['username'],
            Email = validated_data['email']
        )
        user_info.save()
        return user


