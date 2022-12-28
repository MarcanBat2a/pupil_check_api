from dependency_injector import containers

from pupil_check_back.config import AppSettings

AppSettings.load_config()


class Container(containers.DeclarativeContainer):
    """Dependency injection container."""

    wiring_config = containers.WiringConfiguration(
        modules=["pupil_check_back.routes.video"]
    )
