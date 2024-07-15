from django.shortcuts import render, redirect
from .models import Patient, Appointment, MedicalHistory, Bill, Payment, Insurance,HealthEducation
from .forms import PatientRegistrationForm, AppointmentBookingForm, MedicalHistoryForm, BillForm, PaymentForm, InsuranceForm,HealthEducationForm

def index(request):
    return render(request,'index.html')

def patient_dashboard(request):
    return render(request,'patient_dashboard.html')

def patient_registration(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient_registration.html', {'form': form})

def appointment_booking(request):
    if request.method == 'POST':
        form = AppointmentBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentBookingForm()
    return render(request, 'appointment_booking.html', {'form': form})

def medical_history(request):
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_history_success')
    else:
        form = MedicalHistoryForm()
    return render(request, 'medical_history.html', {'form': form})

def billing(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing_success')
    else:
        form = BillForm()
    return render(request, 'billing.html', {'form': form})

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_success')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})

def insurance(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insurance_success')
    else:
        form = InsuranceForm()
    return render(request, 'insurance.html', {'form': form})

def patient_dashboard(request):
    medical_history = MedicalHistory.objects.filter(patient=request.user)
    appointments = Appointment.objects.filter(patient=request.user)
    bills = Bill.objects.filter(appointment__in=appointments)
    insurance = Insurance.objects.filter(patient=request.user)
    return render(request, 'patient_dashboard.html', {'medical_history': medical_history, 'appointments': appointments, 'bills': bills, 'insurance': insurance})

def health_education_resources(request):
    return render(request, 'health_education_resources.html')