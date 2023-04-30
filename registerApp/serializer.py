from rest_framework import serializers
from registerApp.models import HealthRecord
from .models import HealthRecord
from django.contrib.auth.models import User


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = "__all__"
        
class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = ['image']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    #customize how user is created and saved to db
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password']