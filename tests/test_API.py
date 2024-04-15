import allure
import pytest
from tests.base_test import BaseTest


class TestAll(BaseTest):

    @allure.feature('Create booking')
    @allure.suite('CRUD with bookings')
    @pytest.mark.critical
    def test_create_booking(self):
        self.create_endpnt.create_booking()
        self.create_endpnt.check_resp_code_is_200()
        self.create_endpnt.check_response_schema()
        self.get_auth_endpnt.get_auth_token()
        self.delete_enpnt.delete_booking(booking_id=self.create_endpnt.booking_id, token=self.get_auth_endpnt.token)

    @allure.suite('CRUD with bookings')
    @allure.feature('GET booking')
    @allure.story('Get booking by id')
    def test_get_booking_by_id(self):
        self.create_endpnt.create_booking()
        first_name_post = self.create_endpnt.first_name
        price_post = self.create_endpnt.total_price

        self.get_by_id_endpnt.get_booking_by_id(self.create_endpnt.booking_id)

        self.get_by_id_endpnt.check_resp_code_is_200()
        self.get_by_id_endpnt.check_total_price_is_(price_post)
        self.get_by_id_endpnt.check_first_name_is_(first_name_post)
        self.get_by_id_endpnt.check_response_schema()

        self.get_auth_endpnt.get_auth_token()

        self.delete_enpnt.delete_booking(booking_id=self.create_endpnt.booking_id, token=self.get_auth_endpnt.token)

    @allure.suite('CRUD with bookings')
    @allure.feature('UPDATE booking')
    @allure.story('Update booking FULL')
    @pytest.mark.parametrize("firstname, totalprice, checkin",
                             [("Bill", 45, "2019-01-02"),
                              ("Mark", 88, "2019-01-05"),
                              ("Simon", 120, "2019-01-03")])
    def test_update_booking_full(self, firstname, totalprice, checkin):
        self.create_endpnt.create_booking()
        booking_id = self.create_endpnt.booking_id

        upd_body = {
            "firstname": firstname,
            "lastname": "Brown",
            "totalprice": totalprice,
            "depositpaid": True,
            "bookingdates": {
                "checkin": checkin,
                "checkout": "2019-01-30"
            },
            "additionalneeds": "Breakfast"
        }

        self.get_auth_endpnt.get_auth_token()

        self.update_all_endpnt.update_booking_full(booking_id=booking_id, token=self.get_auth_endpnt.token, body=upd_body)

        self.update_all_endpnt.check_resp_code_is_200()
        self.update_all_endpnt.check_first_name_is_(firstname)
        self.update_all_endpnt.check_total_price_is_(totalprice)
        self.update_all_endpnt.check_booking_dates_checkin(checkin)

        self.delete_enpnt.delete_booking(booking_id=booking_id, token=self.get_auth_endpnt.token)

    @allure.suite('CRUD with bookings')
    @allure.feature('UPDATE booking')
    @allure.story('Update user booking')
    @pytest.mark.parametrize("lastname, additionalneeds",
                             [('Hense', 'Fan in the room'),
                              ('Rimma', 'Do not disturb')])
    def test_update_booking_partially(self, lastname, additionalneeds):
        self.create_endpnt.create_booking()
        booking_id = self.create_endpnt.booking_id

        upd_body = {
            "lastname": lastname,
            "additionalneeds": additionalneeds
        }

        self.get_auth_endpnt.get_auth_token()

        self.update_part_endpnt.update_booking_partionally(booking_id=booking_id,
                                                           token=self.get_auth_endpnt.token,
                                                           body=upd_body)

        self.update_part_endpnt.check_resp_code_is_200()
        self.update_part_endpnt.check_last_name_is_(lastname)
        self.update_part_endpnt.check_additional_needs_is_(additionalneeds)

        self.delete_enpnt.delete_booking(booking_id=booking_id, token=self.get_auth_endpnt.token)

    @allure.suite('CRUD with bookings')
    @allure.feature('DELETE booking')
    @allure.story('Delete booking')
    @pytest.mark.medium
    def test_delete_booking(self):
        self.create_endpnt.create_booking()
        booking_id = self.create_endpnt.booking_id

        self.get_auth_endpnt.get_auth_token()

        self.delete_enpnt.delete_booking(booking_id=booking_id, token=self.get_auth_endpnt.token)
        self.delete_enpnt.check_resp_code_is_201()
