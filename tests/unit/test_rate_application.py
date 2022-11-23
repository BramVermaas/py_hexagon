import unittest

from py_hexagon.application.rate_application import RatingApplication
from tests.doubles.fake_rate_provider import FakeRateProvider
from tests.doubles.fake_rating_usecase import FakeRatingUseCase


class TestRateApplication(unittest.TestCase):
    def setUp(self) -> None:
        """Configure application with fake adapters."""
        rater = FakeRateProvider()
        application = RatingApplication(rater)
        self.rating_use_case = FakeRatingUseCase(application)

    def test_small_input_value(self) -> None:
        rating = self.rating_use_case.input_value(10.0)
        self.assertEqual(rating.result, 11.0)

    def test_big_input_value(self) -> None:
        rating = self.rating_use_case.input_value(100.0)
        self.assertEqual(rating.result, 150.0)
