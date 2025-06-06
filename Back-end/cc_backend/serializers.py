from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'email': {'required': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
