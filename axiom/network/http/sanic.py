import asyncio

import sanic

from .base import HTTPServer

# for now we'll just use the user-api, but we could possibly start using
# internal components like it's router and other stuff


class SanicServer(HTTPServer):
    @property
    def server_task(self) -> asyncio.Task:
        pass
