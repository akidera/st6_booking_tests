from endpoints.create_endpnt import CreateBooking
from endpoints.get_endpoint import GetBookingById
from endpoints.get_auth_token import GetAuthToken
from endpoints.delete_endpoint import DeleteBooking
from endpoints.update_endpoint import UpdateBookingFull
from endpoints.update_part_endpoint import UpdateBookingPart


class BaseTest:
    def setup_method(self):
        self.create_endpnt = CreateBooking()
        self.get_by_id_endpnt = GetBookingById()
        self.get_auth_endpnt = GetAuthToken()
        self.delete_enpnt = DeleteBooking()
        self.update_all_endpnt = UpdateBookingFull()
        self.update_part_endpnt = UpdateBookingPart()
