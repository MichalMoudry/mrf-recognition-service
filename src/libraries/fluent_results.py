"""
Module with code for fluent results library.
"""
from typing import TypeVar, Generic

T = TypeVar("T")


class Result(Generic[T]):
    """
    Class representing a result object that encapsulates a value and an operation result.
    """
    def __init__(self):
        self._value: T = None
        self._is_success = False

    @property
    def value(self) -> T:
        """
        Encapsulated value.
        """
        return self._value

    def ok(self, value: T = None):
        self._value = value
        self._is_success = True

    def fail(self):
        """
        Sets the result object to failed state.
        """
        self._is_success = False

    def has_value(self) -> bool:
        """
        Method for checking if Result object has a value set.
        :return: True if value is set. False if not.
        """
        return self._value is not None
