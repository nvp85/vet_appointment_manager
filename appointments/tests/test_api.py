from django.urls import reverse
from rest_framework.test import APIClient
import pytest
from appointments.models import Appointment, Client, Pet, Specialist


@pytest.fixture
def new_client(db):
    c = Client.objects.create(
        full_name='test client',
        phone_number = '+1 232 233 3290'
    )
    return c


@pytest.fixture
def new_pet(db):
    pet = Pet.objects.create(
        name = 'test pet',
        type = 'bird',
        sex = 'f'
    )
    return pet


@pytest.fixture
def new_specialist(db):
    s = Specialist.objects.create(
        first_name = 'test',
        last_name = 'specialist',
        job_title = 'DVM'
    )
    return s


@pytest.mark.django_db
def test_get_pets(new_pet):
    clt = APIClient()
    url = reverse('pet-list')
    response = clt.get(url, format='json')
    assert response.status_code == 200
    assert len(response.data) == 1 #Pet.objects.count()


@pytest.mark.django_db
def test_get_specialists(new_specialist):
    clt = APIClient()
    url = reverse('specialist-list')
    response = clt.get(url, format='json')
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_clients(new_client):
    clt = APIClient()
    url = reverse('client-list')
    response = clt.get(url, format='json')
    assert response.status_code == 200
    assert len(response.data) == 1 #Client.objects.count()


@pytest.mark.django_db
def test_get_client_detail(new_client, new_pet):
    new_pet.client_set.add(new_client)
    clt = APIClient()
    url = reverse('client-detail', kwargs={'pk': new_client.id})
    response = clt.get(url, format='json')
    assert response.status_code == 200
    assert response.data['full_name'] == new_client.full_name
    assert len(response.data['pets']) == 1


@pytest.mark.django_db
def test_post_appointment_error(new_client, new_pet, new_specialist):
    clt = APIClient()
    url = reverse('appointments-list')
    data = {
	"client": new_client.id,
	"pet": new_pet.id,
	"specialist": new_specialist.id,
	"date_time": "2022-03-23T15:00:00.00Z"
    }
    response = clt.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data.get('non_field_errors')[0].title() == "The Pet Must Belong To The Client!"


@pytest.mark.django_db
def test_post_appointment(new_client, new_pet, new_specialist):
    clt = APIClient()
    url = reverse('appointments-list')
    new_pet.client_set.add(new_client)
    data = {
	"client": new_client.id,
	"pet": new_pet.id,
	"specialist": new_specialist.id,
	"date_time": "2022-03-23T15:00:00.00Z"
    }
    response = clt.post(url, data, format='json')
    assert response.status_code == 201
