from py_hexagon.domain.request_rating import RequestRating


class ConsoleAdapter:
    """Adapter for RequestRating (driver) port."""

    def __init__(self, rating_app: RequestRating):
        self._rating_app = rating_app

    def start(self):
        value_to_rate = float(input("Please enter a number to apply the rate to: "))
        rating = self._rating_app.get_rating(value=value_to_rate)
        print(f"Rate: {rating.rate}, Result: {rating.result:.2f}")
