from py_hexagon.ports.rating_usecase import RatingUseCase, Rating


class FakeRatingUseCase:
    """Adapter for RatingUseCase port."""

    def __init__(self, rating_app: RatingUseCase):
        self._rating_app = rating_app

    def input_value(self, input_value: float) -> Rating:
        return self._rating_app.get_rating(value=input_value)
