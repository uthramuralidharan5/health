from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Patient import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('Patient.urls')),
    path('', include('Admin.urls')),
    path('', include('Doctor.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
