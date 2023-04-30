from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from registerApp.views import create_record ,HealthRecordImageView, HealthRecordDeleteView,UserRegistration

app_name= "health_app"
urlpatterns = [
    path('',create_record.as_view({'post':'create'}), name='rec_post'),
    path('list/',create_record.as_view({'get':'list'}), name='get'),
    path('images/list', HealthRecordImageView.as_view(), name='image-list'),
    path('delete/<int:pk>/', HealthRecordDeleteView.as_view(), name='delete-healthrecord'),
    path('register/', UserRegistration.as_view(),name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]
