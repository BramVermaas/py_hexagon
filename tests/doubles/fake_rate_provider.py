from py_hexagon.ports.rate_provider import RateProvider


class FakeRateProvider(RateProvider):
    """Adapter for RateProvider port."""

    def get_rate_for(self, value: float) -> float:
        if value < 50.0:
            return 1.1
        else:
            return 1.5
