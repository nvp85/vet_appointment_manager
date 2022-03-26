from django.urls import reverse
from rest_framework.test import APIClient
import pytest
from appointments.models import Appointment, Client, Pet, Specialist
from rest_framework.authtoken.models import Token


@pytest.fixture
def auth_api_client(db, django_user_model):
    usr = django_user_model.objects.create_user(
        username="test_username", password="test_password"
    )
    token = Token.objects.create(user=usr)
    clt = APIClient()
    clt.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return clt


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
def test_get_pets(new_pet, auth_api_client):
    url = reverse('pet-list')
    response = auth_api_client.get(url, format='json')
    assert response.status_code == 200
    assert len(response.data) == 1 #Pet.objects.count()


@pytest.mark.django_db
def test_get_specialists(new_specialist, auth_api_client):
    url = reverse('specialist-list')
    response = auth_api_client.get(url, format='json')
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_clients(new_client, auth_api_client):
    url = reverse('client-list')
    response = auth_api_client.get(url, format='json')
    assert response.status_code == 200
    assert len(response.data) == 1 #Client.objects.count()


@pytest.mark.django_db
def test_get_client_detail(new_client, new_pet, auth_api_client):
    new_pet.client_set.add(new_client)
    url = reverse('client-detail', kwargs={'pk': new_client.id})
    response = auth_api_client.get(url, format='json')
    assert response.status_code == 200
    assert response.data['full_name'] == new_client.full_name
    assert len(response.data['pets']) == 1


@pytest.mark.django_db
def test_post_appointment_error(new_client, new_pet, new_specialist, auth_api_client):
    url = reverse('appointments-list')
    data = {
	"client": new_client.id,
	"pet": new_pet.id,
	"specialist": new_specialist.id,
	"date_time": "2022-03-23T15:00:00.00Z"
    }
    response = auth_api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data.get('non_field_errors')[0].title() == "The Pet Must Belong To The Client!"


@pytest.mark.django_db
def test_post_appointment(new_client, new_pet, new_specialist, auth_api_client):
    url = reverse('appointments-list')
    new_pet.client_set.add(new_client)
    data = {
	"client": new_client.id,
	"pet": new_pet.id,
	"specialist": new_specialist.id,
	"date_time": "2022-03-23T15:00:00.00Z"
    }
    response = auth_api_client.post(url, data, format='json')
    assert response.status_code == 201
