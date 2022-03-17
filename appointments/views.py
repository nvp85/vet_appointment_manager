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
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all().order_by('date_time')
        client_id = self.request.query_params.get('client_id')
        if client_id is not None:
            queryset = queryset.filter(client__id=int(client_id))
        specialist_id = self.request.query_params.get('specialist_id')
        if specialist_id is not None:
            queryset = queryset.filter(specialist__id=int(specialist_id))
        pet_id = self.request.query_params.get('pet_id')
        if pet_id is not None:
            queryset = queryset.filter(pet__id=int(pet_id))
        return queryset