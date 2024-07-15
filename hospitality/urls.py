from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Patient import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/', include('Patient.urls')),
    path('admin/', include('Admin.urls')),
    path('doctor/', include('Doctor.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
