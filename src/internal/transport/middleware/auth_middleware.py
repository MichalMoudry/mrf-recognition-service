"""
Module containing implementation of an authentication middleware.
"""
from typing import Any, Awaitable, Callable


class AuthMiddleware:
    """
    Class handling of service's authentication function.
    """

    def __init__(self, app):
        self._app: Callable[[Any, Any, None], Awaitable] = app

    async def __call__(self, scope, receive, send):
        """if "headers" not in scope:
            return await self._app(scope, receive, send)"""
        return self.error_response(receive, send)

    async def error_response(self, receive, send):
        await send({
            "type": "http.response.start",
            "status": 401,
            "headers": [(b"content-length", b"0")]
        })
        await send({
            "type": "http.response.body",
            "body": b"",
            "more_body": False
        })
