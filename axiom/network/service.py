import abc

from axiom.server import MatrixHomeServer

from .client_server import ClientServerService
from .federation import FederationService


class NetworkService(abc.ABC):
    # noinspection PyUnusedLocal
    @abc.abstractmethod
    def __init__(self, server: MatrixHomeServer):
        ...

    @abc.abstractmethod
    @property
    def client_server(self) -> ClientServerService:
        ...

    @abc.abstractmethod
    @property
    def federation(self) -> FederationService:
        ...
