"""
Module containing implementation of an authentication middleware.
"""

class AuthMiddleware:
    """
    Class handling of service's authentication function.
    """

    def __init__(self, app):
        self._app = app

    async def __call__(self, scope, receive, send):
        if "headers" not in scope:
            return await self.app(scope, receive, send)
        ...

    async def error_response(self, receive, send):
        ...
