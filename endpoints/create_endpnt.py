import requests
from endpoints.json_schemas import BookingResponse
import allure
from endpoints.BaseEndpoint import BaseEndpoint


class CreateBooking(BaseEndpoint):

    @allure.step('Send create request')
    def create_booking(self, body=None, base_url=BaseEndpoint.BASE_URL):
        body = body if body else BaseEndpoint.BODY
        self.response = requests.post(f"{base_url}/booking", json=body)
        self.response_code = self.response.status_code
        self.response_json = self.response.json()
        self.booking_id = self.response_json['bookingid']
        self.first_name = self.response_json['booking']['firstname']
        self.last_name = self.response_json['booking']['lastname']
        self.total_price = self.response_json['booking']['totalprice']
        self.deposit_paid = self.response_json['booking']['depositpaid']
        self.booking_dates_checkin = self.response_json['booking']['bookingdates']['checkin']
        self.booking_dates_checkout = self.response_json['booking']['bookingdates']['checkout']
        self.additional_needs = self.response_json['booking']['additionalneeds']

    @allure.step('Check schema is correct')
    def check_response_schema(self):
        BookingResponse(**self.response_json)
