from django.contrib import admin
from django.urls import path
from registerApp.views import create_record ,HealthRecordImageView, HealthRecordDeleteView

app_name= "health_app"
urlpatterns = [
    path('',create_record.as_view({'post':'create'}), name='rec_post'),
    path('list/',create_record.as_view({'get':'list'}), name='get'),
    path('images/list', HealthRecordImageView.as_view(), name='image-list'),
    path('delete/<int:pk>/', HealthRecordDeleteView.as_view(), name='delete-healthrecord'),
    
]
