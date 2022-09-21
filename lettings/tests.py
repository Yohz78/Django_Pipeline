import pytest
from django.core.management import call_command
from django.urls import reverse


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data.json')


@pytest.mark.django_db
def test_get_letting_index(client):
    response = client.get(reverse('lettings_index'))
    assert b"<h1>Lettings</h1>" in response.content
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_letting(client):
    response = client.get(reverse('letting', args=[1]))
    assert b"Joshua Tree Green Haus /w Hot Tub" in response.content
    assert b"7217 Bedford Street" in response.content
    assert response.status_code == 200
