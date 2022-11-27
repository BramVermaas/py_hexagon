from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


@dataclass
class Rating:
    rate: float
    result: float


class RequestRating(metaclass=ABCMeta):
    """Driver (left) port of Rater."""

    @abstractmethod
    def get_rating(self, value: float) -> Rating:
        raise NotImplementedError
