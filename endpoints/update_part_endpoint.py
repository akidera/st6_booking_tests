import requests
import allure
from endpoints.BaseEndpoint import BaseEndpoint


class UpdateBookingPart(BaseEndpoint):
    def update_booking_partionally(self, booking_id, token, body, base_url=BaseEndpoint.BASE_URL):
        headers = {'Cookie': f'token={token}'}
        body = body if body else BaseEndpoint.BODY
        self.response = requests.patch(f"{base_url}/booking/{booking_id}", json=body, headers=headers)
        self.response_code = self.response.status_code
        self.response_json = self.response.json()
        self.first_name = self.response_json['firstname']
        self.last_name = self.response_json['lastname']
        self.total_price = self.response_json['totalprice']
        self.deposit_paid = self.response_json['depositpaid']
        self.booking_dates_checkin = self.response_json['bookingdates']['checkin']
        self.booking_dates_checkout = self.response_json['bookingdates']['checkout']
        self.additional_needs = self.response_json['additionalneeds']
