from pyexpat import model
from rest_framework import serializers
from .models import Client, Pet, Specialist, Appointment


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = '__all__'

class SpecialistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Specialist
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'


