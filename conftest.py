import pytest
import requests
from endpoints.create_endpnt import BaseEndpoint
from endpoints.create_endpnt import CreateBooking
from endpoints.get_endpoint import GetBookingById
from endpoints.get_auth_token import GetAuthToken
from endpoints.delete_endpoint import DeleteBooking
from endpoints.update_endpoint import UpdateBookingFull
from endpoints.update_part_endpoint import UpdateBookingPart
from endpoints.json_schemas import BookingResponse

base_url = BaseEndpoint.BASE_URL


@pytest.fixture()
def start_end():
    print('\nStart testing')
    yield
    print('\nEnd testing')


@pytest.fixture()
def get_auth_token():
    return GetAuthToken()


@pytest.fixture()
def create_booking_obj():
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
    data = BookingResponse(**response)
    return data


@pytest.fixture()
def auth():
    auth_body = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{base_url}/auth", json=auth_body).json()
    token = response['token']
    return token


@pytest.fixture()
def del_booking():
    bookings_ids = []
    yield bookings_ids
    auth_body = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{base_url}/auth", json=auth_body).json()
    token = response['token']
    headers = {'Cookie': f'token={token}'}

    for id in bookings_ids:
        requests.delete(f"{base_url}/booking/{id}", headers=headers)
        print(f'\n{id} was deleted')


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
