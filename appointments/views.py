from .models import Client, Pet, Specialist, Appointment
from .serializers import ClientSerializer, PetSerializer, SpecialistSerializer, AppointmentSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('full_name')
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['full_name', 'phone_number', 'email']
    search_fields = ['full_name', 'phone_number','email', 'address']

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('name')
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'type', 'sex', 'breed', 'microchip_num']
    search_fields = ['name', 'type', 'breed', 'microchip_num', 'microchip_location', 'coat_color']


class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all().order_by('last_name')
    serializer_class = SpecialistSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'job_title']
    search_fields = ['first_name', 'last_name', 'job_title']

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all().order_by('date_time')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['client_id', 'pet_id', 'specialist_id', 'date_time', 'created']
    search_fields = ['client_id', 'pet_id', 'specialist_id', 'date_time', 'created', 'reason', 'conclusion']

