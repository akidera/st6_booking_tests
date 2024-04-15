import pytest
import requests
from endpoints.create_endpnt import CreateBooking
from endpoints.get_endpoint import GetBookingById
from endpoints.get_auth_token import GetAuthToken
from endpoints.delete_endpoint import DeleteBooking
from endpoints.update_endpoint import UpdateBookingFull
from endpoints.update_part_endpoint import UpdateBookingPart


@pytest.fixture()
def start_end():
    print('\nStart testing')
    yield
    print('\nEnd testing')


@pytest.fixture()
def obj_id():
    body = {
        "name": "Some title",
        "data": {
            "year": 2018,
            "price": 42,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev//objects", json=body).json()
    obj_id = response['id']
    return obj_id


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
