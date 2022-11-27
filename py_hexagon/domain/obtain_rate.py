from abc import ABCMeta, abstractmethod


class ObtainRate(metaclass=ABCMeta):
    """Driven (right) port of Rater."""

    @abstractmethod
    def get_rate_for(self, value: float) -> float:
        raise NotImplementedError
