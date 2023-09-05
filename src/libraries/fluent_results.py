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
        self._reason_type = reason_type
        self._reason = reason

    @property
    def reason_type(self) -> ReasonType:
        return self._reason_type

    @property
    def reason(self) -> str:
        return self._reason


class Result(Generic[T]):
    """
    Class representing a result object that encapsulates a value and an operation result.
    """
    def __init__(self, result: bool, value: T = None):
        self._result = result
        self._value = value
        self._reasons: list[Reason] = []

    @property
    def value(self) -> T | None:
        """
        A property with a value that is encapsulated by the result object.
        """
        return self._value

    @property
    def is_success(self) -> bool:
        """
        A property with a value indicating, if result is success or not.
        :return: Returns True if result is marked as a success or False if not.
        """
        return self._result
    
    @property
    def errors(self) -> list[str]:
        """
        A list of error messages.
        """
        if len(self._reasons) == 0:
            return []
        return [reason.reason for reason in self._reasons if reason.reason_type is ReasonType.ERROR]

    @property
    def successes(self):
        """
        A list of success messages.
        """
        return [reason.reason for reason in self._reasons if reason.reason_type is ReasonType.SUCCESS]

    def has_value(self) -> bool:
        """
        Method for checking if Result object has a value set.
        :return: True if value is set. False if not.
        """
        return self._value is not None

    def with_error(self, err_message: str):
        """
        Method for adding a new error message to the result.
        """
        self._reasons.append(Reason(ReasonType.ERROR, err_message))
        return self

    def with_success(self, msg: str):
        """
        Method for adding a new success message to the result.
        """
        self._reasons.append(Reason(ReasonType.SUCCESS, msg))
        return self
