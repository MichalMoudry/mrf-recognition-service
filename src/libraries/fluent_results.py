"""
Module with code for fluent results library.
"""
from typing import TypeVar

T = TypeVar("T")


class Result:
    """
    Class representing a result object that encapsulates a value and an operation result.
    """
    def __init__(self):
        self._was_result_modified = False
        self._value: T = None
        self._is_success = False
        self._messages: list[str] = []

    def ok(self, value: T = None):
        self._was_result_modified = True
        self._is_success = True
        self._value = value
        return self

    def fail(self, msg: str):
        self._was_result_modified = True
        self._is_success = False
        self._messages.append(msg)
        return self

    @property
    def value(self) -> T:
        return self._value

    @property
    def messages(self) -> list[str]:
        return self._messages

    @property
    def is_success(self) -> bool:
        return self._is_success

    def has_value(self):
        """
        Method for checking if Result object has a value set.
        :return: True if value is set. False if not.
        """
        return self._value is not None
