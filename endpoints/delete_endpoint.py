import requests
import allure
from endpoints.BaseEndpoint import BaseEndpoint


class DeleteBooking(BaseEndpoint):

    @allure.step('Send delete request')
    def delete_booking(self, booking_id, token, base_url=BaseEndpoint.BASE_URL):
        headers = {'Cookie': f'token={token}'}
        self.response = requests.delete(f"{base_url}/booking/{booking_id}", headers=headers)
        self.response_code = self.response.status_code
