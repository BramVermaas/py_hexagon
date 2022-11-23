from py_hexagon.adapters.prompt_rating_usecase import PromptRatingUseCase
from py_hexagon.adapters.file_rate_provider import FileRateProvider
from py_hexagon.application.rate_application import RatingApplication


def main():
    """Configure application with adapters and start."""
    rater = FileRateProvider()
    application = RatingApplication(rater)
    PromptRatingUseCase(application).start()


if __name__ == "__main__":
    main()
