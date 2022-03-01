from django.db import models
from datetime import datetime


class Pet(models.Model):
    SEX_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]
    name = models.CharField(max_length=150, null=False, blank=False)
    type = models.CharField(max_length=20, null=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=False, blank=False)
    breed = models.CharField(max_length=50)
    microchip_num = models.CharField(max_length=100)
    microchip_location = models.Charfield()
    coat_color = models.CharField()
    dob = models.DateField()


class Client(models.Model):
    full_name = models.CharField(max_length=150, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    join_date = models.DateTimeField(auto_now_add=True)
    pets = models.ManyToManyField(Pet, on_delete=models.CASCADE) # one client can have many pets and one pet can belong to several clients


class Specialist(models.Model):
    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    job_title = models.CharField(max_length=150, null=False, blank=False)


class Appointment(models.Model):
    client = models.ForeignKey(Client, null=False)
    pet = models.ForeignKey(Pet)
    specialist = models.ForeignKey(Specialist, null=False)
    date_time = models.DateTimeField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    conclusion = models.TextField()
