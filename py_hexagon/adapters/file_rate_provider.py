import json

from py_hexagon.ports.rate_provider import RateProvider
from pathlib import Path


class FileRateProvider(RateProvider):
    """Adapter for RateProvider port."""

    def get_rate_for(self, value: float) -> float:
        rate_specs = self._rate_spec_from_file()
        if value < rate_specs["threshold"]:
            return rate_specs["below_threshold_rate"]
        else:
            return rate_specs["above_threshold_rate"]

    @staticmethod
    def _rate_spec_from_file() -> dict[str, float]:
        root_dir = Path(__file__).resolve().parents[2]
        rates_file = root_dir / "rate_files" / "rates.json"
        with open(rates_file) as rates_data:
            return json.load(rates_data)
