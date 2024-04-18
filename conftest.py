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
    data = CreateBooking().create_booking()
    return data


@pytest.fixture()
def auth():
    token = GetAuthToken().get_auth_token()
    return token


@pytest.fixture()
def del_booking():
    bookings_ids = []
    yield bookings_ids

    token = GetAuthToken().get_auth_token()

    for id in bookings_ids:
        DeleteBooking().delete_booking(booking_id=id, token=token)
        print(f'\n{id} was deleted')


@pytest.fixture()
def create_del_booking():
    data = CreateBooking().create_booking()
    yield data

    token = GetAuthToken().get_auth_token()

    DeleteBooking().delete_booking(booking_id=data.bookingid,
                                   token=token)
    print(f'\n{data.bookingid} was deleted')

