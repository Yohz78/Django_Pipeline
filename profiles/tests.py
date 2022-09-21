import pytest
from django.core.management import call_command
from django.urls import reverse


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data.json')


@pytest.mark.django_db
def test_get_profile_index(client):
    response = client.get(reverse('profiles_index'))
    assert b"<h1>Profiles</h1>" in response.content
    assert b"HeadlinesGazer" in response.content
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_profile(client):
    response = client.get(reverse('profile', args=["HeadlinesGazer"]))
    assert b"HeadlinesGazer" in response.content
    assert response.status_code == 200
