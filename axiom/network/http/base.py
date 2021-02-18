import abc
import asyncio
from typing import Optional


class HTTPServer(abc.ABC):
    @abc.abstractmethod
    @property
    def server_task(self) -> Optional[asyncio.Task]:
        """
        Returns the asyncio task currently managing the HTTP server,
        returns None when server has not started yet,
        the task may be cancelled or finished.
        """
