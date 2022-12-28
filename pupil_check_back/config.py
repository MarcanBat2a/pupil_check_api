import os

from dotenv import load_dotenv


class AppSettings:
    """Application settings."""

    DATABASE_URL: str
    PYTHON_ENV: str
    TASK_API_URL: str
    API_NAME: str
    ENV_FILE: str = ".env"

    @staticmethod
    def load_config() -> None:
        """Load configuration from environment variables."""
        load_dotenv(AppSettings.ENV_FILE)
        AppSettings.PYTHON_ENV = os.getenv("PYTHON_ENV")
        AppSettings.API_NAME = os.getenv("API_NAME")
