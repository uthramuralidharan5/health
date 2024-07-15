from django.contrib import admin
from .models import Patient, Appointment, Bill, MedicalHistory,HealthEducation,Payment,Insurance

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Bill)
admin.site.register(Payment)
admin.site.register(Insurance)
admin.site.register(MedicalHistory)
admin.site.register(HealthEducation)
