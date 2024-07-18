from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.patient_dashboard),
    path('', views.patient_registration),
    path('', views.appointment_booking),
    path('', views.medical_history),
    path('', views.billing),
    path('',views.Payment),
    path('', views.health_education_resources),
]
