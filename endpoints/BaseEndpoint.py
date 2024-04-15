import allure


class BaseEndpoint:
    BASE_URL = 'https://restful-booker.herokuapp.com'

    BODY = {
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

    response = None
    response_code = None
    response_json = None
    booking_id = None
    first_name = None
    total_price = None
    last_name = None
    deposit_paid = None
    booking_dates_checkin = None
    booking_dates_checkout = None
    additional_needs = None

    @allure.step('Asserting response is 200')
    def check_resp_code_is_200(self):
        assert self.response_code == 200, 'Status code is not 200'

    @allure.step('Asserting response is 201')
    def check_resp_code_is_201(self):
        assert self.response_code == 201, 'Status code is not 201'

    @allure.step('Asserting response is 404')
    def check_resp_code_is_404(self):
        assert self.response_code == 404, 'Status code is not 404'

    @allure.step('Asserting price is valid')
    def check_total_price_is_(self, price):
        assert self.total_price == price

    @allure.step('Asserting first name is valid')
    def check_first_name_is_(self, first_name):
        assert self.first_name == first_name

    @allure.step('Asserting first name is valid')
    def check_last_name_is_(self, last_name):
        assert self.last_name == last_name

    @allure.step('Asserting first name is valid')
    def check_additional_needs_is_(self, additional_needs):
        assert self.additional_needs == additional_needs
