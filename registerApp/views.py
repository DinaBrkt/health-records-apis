from django.shortcuts import render
from registerApp.serializer import RecordSerializer,imageSerializer
from rest_framework.viewsets import ModelViewSet
from .models import HealthRecord
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.
class create_record(ModelViewSet):
    serializer_class = RecordSerializer
    queryset = HealthRecord.objects.all()

class HealthRecordImageView(generics.ListAPIView):
    serializer_class = imageSerializer
    queryset = HealthRecord.objects.all()

#use GenericAPIView when I want to define my own get and post
class HealthRecordDeleteView(GenericAPIView):
    queryset = HealthRecord.objects.all()
    serializer_class = RecordSerializer
    def post(self,request,pk):
        object = self.get_object()
        object.delete()
        return Response({"message":"deleted successfully"})
       
   
    
