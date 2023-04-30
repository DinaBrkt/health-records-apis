from django.shortcuts import render
from registerApp.serializer import RecordSerializer,imageSerializer,UserSerializer
from rest_framework.viewsets import ModelViewSet
from .models import HealthRecord
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


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
    

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
  

class MyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # access user information using request.user
        return Response({'user_id': request.user.id, 'username': request.user.username})