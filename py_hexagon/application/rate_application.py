from py_hexagon.ports.rate_provider import RateProvider
from py_hexagon.ports.rating_usecase import Rating, RatingUseCase


class RatingApplication(RatingUseCase):
    """The business logic."""

    def __init__(self, rater: RateProvider):
        self._rater = rater

    def get_rating(self, value: float) -> Rating:
        rate = self._rater.get_rate_for(value)
        return Rating(rate=rate, result=value * rate)


