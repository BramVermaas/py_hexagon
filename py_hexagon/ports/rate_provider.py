from abc import ABCMeta, abstractmethod


class RateProvider(metaclass=ABCMeta):
    """Driven (outgoing) port of RatingApplication."""

    @abstractmethod
    def get_rate_for(self, value: float) -> float:
        raise NotImplementedError
