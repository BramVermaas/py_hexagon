from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


@dataclass
class Rating:
    rate: float
    result: float


class RatingUseCase(metaclass=ABCMeta):
    """Driving (inbound) port of RatingApplication."""

    @abstractmethod
    def get_rating(self, value: float) -> Rating:
        raise NotImplementedError
