import unittest

from py_hexagon.domain.rater import Rater
from py_hexagon.domain.obtain_rate import ObtainRate
from py_hexagon.domain.request_rating import Rating


class FakeRateProvider(ObtainRate):
    """Adapter for ObtainRate (driven) port."""

    def get_rate_for(self, value: float) -> float:
        if value < 100.0:
            return 1.5
        else:
            return 2.5


class TestRater(unittest.TestCase):
    def setUp(self) -> None:
        """Configure application with a fake adapter.

        Note that the test itself is the driver (left) adapter.
        """
        rate_provider = FakeRateProvider()
        self.rater = Rater(rate_provider)

    def test_below_threshold_input_returns_rating_with_low_rate(self) -> None:
        rating = self.rater.get_rating(10.0)
        self.assertEqual(rating, Rating(rate=1.5, result=15.0))

    def test_above_threshold_input_returns_rating_with_high_rate(self) -> None:
        rating = self.rater.get_rating(100.0)
        self.assertEqual(rating, Rating(rate=2.5, result=250.0))
