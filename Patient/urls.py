from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_dashboard, name='patient_dashboard'),
    path('patient/register/', views.patient_registration, name='patient_registration'),
    path('appointment/book/', views.appointment_booking, name='appointment_booking'),
    path('medical_record/', views.medical_history, name='medical_record'),
    path('billing/', views.billing, name='billing'),
    path('payments/',views.Payment,name='payment'),
    path('health_education/', views.health_education_resources, name='health_education'),
]
