from py_hexagon.domain.obtain_rate import ObtainRate
from py_hexagon.domain.request_rating import Rating, RequestRating


class Rater(RequestRating):
    """The application, containing the business logic."""

    def __init__(self, rate_supplier: ObtainRate):
        self._rate_supplier = rate_supplier

    def get_rating(self, value: float) -> Rating:
        rate = self._rate_supplier.get_rate_for(value)
        return Rating(rate=rate, result=value * rate)


