from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, FacilityForm, AppointmentForm
from .models import User, Facility, Appointment

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

@login_required
def user_management(request):
    users = User.objects.all()
    return render(request, 'user_management.html', {'users': users})

@login_required
def facility_management(request):
    facilities = Facility.objects.all()
    return render(request, 'facility_management.html', {'facilities': facilities})

@login_required
def appointment_management(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_management.html', {'appointments': appointments})

