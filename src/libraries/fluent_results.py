"""
Module with code for fluent results library.
"""
from typing import TypeVar, Generic

T = TypeVar("T")


class Result(Generic[T]):
    """
    Class representing a result object that encapsulates a value and an operation result.
    """
    def __init__(self, result: bool, value: T = None):
        self._result = result
        self._value = value

    @property
    def value(self) -> T | None:
        return self._value

    @property
    def is_success(self) -> bool:
        return self._result

    def has_value(self) -> bool:
        """
        Method for checking if Result object has a value set.
        :return: True if value is set. False if not.
        """
        return self._value is not None
