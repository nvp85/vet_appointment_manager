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

    def validate(self, data):
        data = super().validate(data)
        client = data.get('client')
        pet = data.get('pet')
        if pet not in client.pets.all():
            raise serializers.ValidationError("The pet must belong to the Client!")
        return data

    class Meta:
        model = Appointment
        fields = '__all__'        

