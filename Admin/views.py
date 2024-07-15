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
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

@login_required
def facility_management(request):
    facilities = Facility.objects.all()
    return render(request, 'facility_management.html', {'facilities': facilities})

@login_required
def create_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facility_management')
    else:
        form = FacilityForm()
    return render(request, 'create_facility.html', {'form': form})

@login_required
def appointment_management(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_management.html', {'appointments': appointments})

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_management')
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})