from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment
from .forms import PrescriptionForm

def doctor_dashboard(request):
    return render(request,'doctor_dashboard.html')


@login_required
def patient_management(request):
    patients = Patient.objects.all()
    return render(request, 'patient_management.html', {'patients': patients})

@login_required
def appointment_schedule(request):
    appointments = Appointment.objects.filter(doctor=request.user)
    return render(request, 'appointment_schedule.html', {'appointments': appointments})

@login_required
def e_prescribing(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.patient = patient
            prescription.save()
            return redirect('doctor_appointment_schedule')
    else:
        form = PrescriptionForm()
    return render(request, 'e_prescribing.html', {'form': form, 'patient': patient})

