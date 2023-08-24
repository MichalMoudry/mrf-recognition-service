"""
Module with code for fluent results library.
"""
from typing import TypeVar, Generic
from enum import Enum

T = TypeVar("T")


class ReasonType(Enum):
    """
    Enumeration representing possible types of a reason for a result.
    """
    ERROR = 0
    SUCCESS = 1


class Reason:
    """
    Class representing a reason (success or failure) for the result.
    """
    def __init__(self, reason_type: ReasonType, reason: str):
        self._reason_type: ReasonType = reason_type
        self._reason: str = reason

    @property
    def reason_type(self) -> ReasonType:
        return self._reason_type


class Success(Reason):
    def __init__(self, reason: str):
        super().__init__(ReasonType.SUCCESS, reason)


class Fail(Reason):
    def __init__(self, reason: str):
        super().__init__(ReasonType.ERROR, reason)


class Result(Generic[T]):
    """
    Class representing a result object that encapsulates a value and an operation result.
    """
    def __init__(self, result: bool, value: T = None):
        self._result: bool = result
        self._value: T | None = value
        self._reasons: list[Reason] = []

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
