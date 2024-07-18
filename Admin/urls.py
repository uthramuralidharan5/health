from django.urls import path
from . import views

urlpatterns = [
    path('admin/',views.admin_dashboard,name='admin_dashboard'),
    path('user_management/', views.user_management, name='user_management'),
    path('facility_management/', views.facility_management, name='facility_management'),
    path('appointment_management/', views.appointment_management, name='appointment_management'),
    ]