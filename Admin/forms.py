from django import forms
from .models import User, Facility, Appointment

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_admin', 'is_staff')

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ('name', 'location', 'department', 'resources')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient_name', 'doctor_name', 'facility', 'department', 'appointment_date', 'appointment_time', 'status')