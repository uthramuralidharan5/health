from django import forms
from .models import Patient, Appointment, MedicalHistory, Bill, Payment, Insurance,HealthEducation

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'email', 'password', 'address', 'phone_number')

class AppointmentBookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient', 'doctor', 'date', 'time','status')

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ('patient', 'diagnosis', 'medications', 'allergies', 'treatment_history')

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields =('appointment', 'amount')

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('bill', 'payment_method', 'payment_date', 'amount')

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ('patient', 'insurance_provider', 'policy_number', 'coverage_start_date', 'coverage_end_date')

class HealthEducationForm(forms.ModelForm):
    class Meta:
        model = HealthEducation
        fields = ('title', 'description', 'resource_type', 'resource_url')

    def __init__(self, *args, **kwargs):
        super(HealthEducationForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['description'].label = 'Description'
        self.fields['resource_type'].label = 'Resource Type'
        self.fields['resource_url'].label = 'Resource URL'

    def clean(self):
        cleaned_data = super(HealthEducationForm, self).clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        resource_type = cleaned_data.get('resource_type')
        resource_url = cleaned_data.get('resource_url')

        if not title:
            self.add_error('title', 'Title is required')
        if not description:
            self.add_error('description', 'Description is required')
        if not resource_type:
            self.add_error('resource_type', 'Resource Type is required')
        if not resource_url:
            self.add_error('resource_url', 'Resource URL is required')

        return cleaned_data
