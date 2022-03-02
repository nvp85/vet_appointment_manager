from django.shortcuts import render
from .models import Client, Pet, Specialist, Appointment
from .serializers import ClientSerializer, PetSerializer, SpecialistSerializer, AppointmentSerializer
from rest_framework import viewsets


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('full_name')
    serializer_class = ClientSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('name')
    serializer_class = PetSerializer

class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all().order_by('last_name')
    serializer_class = SpecialistSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('date_time')
    serializer_class = AppointmentSerializer