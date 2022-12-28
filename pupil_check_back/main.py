from fastapi import FastAPI

from pupil_check_back import __version__
from pupil_check_back.dependency_injection import Container


def create_app(app_name: str) -> FastAPI:
    """Create FastAPI app."""
    # Instantiate the FastAPI application
    app = FastAPI(title=app_name, version=__version__)

    # Bind the dependency injection container
    container = Container()
    app.container = container

    # Load up the routers

    return app


app = create_app("jsk_order_api")
