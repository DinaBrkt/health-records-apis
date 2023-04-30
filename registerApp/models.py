from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class CustomStorage(S3Boto3Storage):
    def custom_upload_to(instance, filename):
            new_filename = instance.name +'.png'
            return new_filename
        
# Create your models here.
class HealthRecord(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    medications = models.CharField(max_length=400)
    gender = models.CharField(max_length=100)
    medical_history = models.CharField(max_length=400)
    allergies = models.CharField(max_length=400)
    first_contact_name = models.CharField(max_length=100)
    first_contact_number = models.CharField(max_length=8)
    vaccines = models.CharField(max_length=400)
    image = models.ImageField(upload_to=CustomStorage.custom_upload_to)




