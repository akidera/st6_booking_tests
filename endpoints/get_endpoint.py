import requests
from endpoints.json_schemas import Booking
import allure
from endpoints.BaseEndpoint import BaseEndpoint


class GetBookingById(BaseEndpoint):
    response_txt = None

    @allure.step('Get all bookings')
    def get_booking_by_id(self, booking_id, base_url=BaseEndpoint.BASE_URL):
        self.response = requests.get(f"{base_url}/booking/{booking_id}")
        self.response_code = self.response.status_code
        self.response_txt = self.response.text
        self.response_json = self.response.json()
        self.first_name = self.response_json['firstname']
        self.total_price = self.response_json['totalprice']

    @allure.step('Check schema is correct')
    def check_response_schema(self):
        Booking(**self.response_json)
