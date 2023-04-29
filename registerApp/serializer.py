from rest_framework import serializers
from registerApp.models import HealthRecord
from .models import HealthRecord


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = "__all__"
        
class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = ['image']