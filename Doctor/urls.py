from django.urls import path
from . import views

urlpatterns = [
    path('',views.doctor_dashboard,name='doctor_dashboard'),
    path('patient_management/', views.patient_management, name='doctor_patient_management'),
    path('appointment_schedule/', views.appointment_schedule, name='doctor_appointment_schedule'),
    path('e_prescribing/<int:patient_id>/', views.e_prescribing, name='doctor_e_prescribing'),
]