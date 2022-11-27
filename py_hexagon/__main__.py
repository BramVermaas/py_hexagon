from py_hexagon.infrastructure.console_adapter import ConsoleAdapter
from py_hexagon.infrastructure.file_rate_provider import FileRateProvider
from py_hexagon.domain.rater import Rater


def main():
    """Configure application with adapters and start."""
    rate_provider = FileRateProvider()
    rater = Rater(rate_provider)
    ConsoleAdapter(rater).start()


if __name__ == "__main__":
    main()
