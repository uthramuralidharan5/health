from django.contrib import admin
from .models import Facility, Appointment, User  

admin.site.register(User)
admin.site.register(Facility)
admin.site.register(Appointment)