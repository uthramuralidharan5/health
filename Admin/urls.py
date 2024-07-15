from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_dashboard,name='admin_dashboard'),
    path('user_management/', views.user_management, name='user_management'),
    path('create_user/', views.create_user, name='create_user'),
    path('facility_management/', views.facility_management, name='facility_management'),
    path('create_facility/', views.create_facility, name='create_facility'),
    path('appointment_management/', views.appointment_management, name='appointment_management'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
]