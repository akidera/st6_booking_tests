import requests
import allure
from endpoints.BaseEndpoint import BaseEndpoint


class GetAuthToken(BaseEndpoint):
    token = None

    @allure.step('Get auth token')
    def get_auth_token(self, base_url=BaseEndpoint.BASE_URL):
        auth_body = {
            "username": "admin",
            "password": "password123"
        }
        self.response = requests.post(f"{base_url}/auth", json=auth_body)
        self.token = self.response.json()['token']
        token = self.token
        return token
