import allure
import pytest
from tests.base_test import BaseTest


class TestAll(BaseTest):

    @allure.feature('Create booking')
    @allure.suite('CRUD with bookings')
    @pytest.mark.critical
    def test_create_booking(self, del_booking):
        body = {
            "firstname": "Anna",
            "lastname": "Miily",
            "totalprice": 100500,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-03-01"
            },
            "additionalneeds": "don\'t disturb"
        }
        self.create_endpnt.create_booking(body=body)

        first_name_post = self.create_endpnt.data.booking.firstname
        price_post = self.create_endpnt.data.booking.totalprice
        booking_id = self.create_endpnt.data.bookingid

        self.get_by_id_endpnt.get_booking_by_id(self.create_endpnt.booking_id)

        self.get_by_id_endpnt.check_resp_code_is_200()
        self.get_by_id_endpnt.check_total_price_is_(price_post)
        self.get_by_id_endpnt.check_first_name_is_(first_name_post)
        self.get_by_id_endpnt.check_response_schema()
        del_booking.append(booking_id)

    @allure.suite('CRUD with bookings')
    @allure.feature('GET booking')
    @allure.story('Get booking by id')
    @pytest.mark.usefixtures("get_booking_by_id")
    def test_get_booking_by_id(self, create_del_booking):

        self.get_by_id_endpnt.get_booking_by_id(booking_id=create_del_booking.bookingid)

        self.get_by_id_endpnt.check_resp_code_is_200()
        self.get_by_id_endpnt.check_total_price_is_(create_del_booking.booking.totalprice)
        self.get_by_id_endpnt.check_first_name_is_(create_del_booking.booking.firstname)

    @allure.suite('CRUD with bookings')
    @allure.feature('UPDATE booking')
    @allure.story('Update booking FULL')
    @pytest.mark.parametrize("firstname, totalprice, checkin",
                             [("Bill", 45, "2019-01-02"),
                              ("Mark", 88, "2019-01-05"),
                              ("Simon", 120, "2019-01-03")])
    def test_update_booking_full(self, create_del_booking, auth,
                                 firstname, totalprice, checkin):
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

        self.update_all_endpnt.update_booking_full(booking_id=create_del_booking.bookingid,
                                                   token=auth,
                                                   body=upd_body)

        self.update_all_endpnt.check_resp_code_is_200()
        self.update_all_endpnt.check_first_name_is_(firstname)
        self.update_all_endpnt.check_total_price_is_(totalprice)
        self.update_all_endpnt.check_booking_dates_checkin(checkin)

    @allure.suite('CRUD with bookings')
    @allure.feature('UPDATE booking')
    @allure.story('Update user booking')
    @pytest.mark.parametrize("lastname, additionalneeds",
                             [('Hense', 'Fan in the room'),
                              ('Rimma', 'Do not disturb')])
    def test_update_booking_partially(self, create_del_booking, auth,
                                      lastname, additionalneeds):
        upd_body = {
            "lastname": lastname,
            "additionalneeds": additionalneeds
        }

        self.update_part_endpnt.update_booking_partionally(booking_id=create_del_booking.bookingid,
                                                           token=auth,
                                                           body=upd_body)

        self.update_part_endpnt.check_resp_code_is_200()
        self.update_part_endpnt.check_last_name_is_(lastname)
        self.update_part_endpnt.check_additional_needs_is_(additionalneeds)

    @allure.suite('CRUD with bookings')
    @allure.feature('DELETE booking')
    @allure.story('Delete booking')
    @pytest.mark.medium
    def test_delete_booking(self, create_booking_obj, auth):

        self.delete_enpnt.delete_booking(booking_id=create_booking_obj.bookingid,
                                         token=auth)

        self.delete_enpnt.check_resp_code_is_201()
