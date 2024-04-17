import pytest
import requests
from endpoints.create_endpnt import BaseEndpoint
from endpoints.create_endpnt import CreateBooking
from endpoints.get_endpoint import GetBookingById
from endpoints.get_auth_token import GetAuthToken
from endpoints.delete_endpoint import DeleteBooking
from endpoints.update_endpoint import UpdateBookingFull
from endpoints.update_part_endpoint import UpdateBookingPart

base_url = BaseEndpoint.BASE_URL


@pytest.fixture()
def start_end():
    print('\nStart testing')
    yield
    print('\nEnd testing')


@pytest.fixture()
def create_del_booking():
    body = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{base_url}/booking", json=body).json()
    booking_id = response['bookingid']
    price_post = response['booking']['totalprice']
    first_name = response['booking']['firstname']

    yield booking_id, price_post, first_name

    auth_body = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{base_url}/auth", json=auth_body).json()
    auth_token = response['token']

    headers = {'Cookie': f'token={auth_token}'}
    requests.delete(f"{base_url}/booking/{booking_id}", headers=headers)


@pytest.fixture()
def get_auth_token():
    return GetAuthToken()


@pytest.fixture()
def create_booking():
    return CreateBooking()


@pytest.fixture()
def get_booking_by_id():
    return GetBookingById()


@pytest.fixture()
def delete_booking_by_id():
    return DeleteBooking()


@pytest.fixture()
def update_booking_full():
    return UpdateBookingFull()


@pytest.fixture()
def update_booking_part():
    return UpdateBookingPart()
